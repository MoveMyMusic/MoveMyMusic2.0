var Mmm, MIDI, startPos;
var trebleNotesOrder = new Array('C', 'D', 'E', 'F', 'G', 'A', 'B');
var bassNotesOrder   = new Array('E', 'F', 'G', 'A', 'B', 'C', 'D');
var notesOrder       = trebleNotesOrder;
var lengthMap        = {
						's'  : .25,
						'sr' : .25,
						'e'  : .5,
						'er' : .5,
						'q'  : 1,
						'qr' : 1,
						'h'  : 2,
						'hr' : 2,
						'dh' : 3,
						'w'  : 4,
						'wr' : 4,
						'dw' : 6
					};
var elements;
var playingNote = 0;

var ajaxRequest = function()
{
		var jsonObject = {
							'studentId' : 1,
							'classId'   : 5
						}
		$.ajax(
		{
			url      : '/rest/endpoint',
			type     : 'post',
			// Get info 'get'
			// Create new 'post'
			// Update record 'put'
			// Delete record 'delete'
			dataType : 'json',
			data     : JSON.stringify(jsonObject),
			success  : function(data, textStatus, jqXHR) 
			{
				console.log(data);
				for (i in data)
				{
					// each row will come back as an object data[i]
					// data[i] = {studentId: 1, classId: 5}
					// data[i].studentId
					$('.classMyDiv').append($('<div class="classname">' + data[i].studentId + '</div>'));
				}
			}
		});
}

var playMusic = function()
{
	notes    = new Array();
	lengths  = new Array();
	elements = new Array();
	$('.added-note').each(function() {
		var top     = parseInt($(this).css('top').replace('px', ''));
		var comb    = parseInt((345 - (startPos.top + top)) / 20);
		var nnumber = parseInt(4 + (comb / 7));
		notes.push(notesOrder[comb % 7] + nnumber);
		lengths.push($(this).data('beats'));
		elements.push(this);
	});
	b = 0;
	time     = 0;
	for (i in notes)
	{
		setTimeout(function() {
			if (playingNote > 0)
				$(elements[playingNote - 1]).animate({opacity: 1});
			$(elements[playingNote]).animate({opacity: .25});
			playingNote++;
		}, 1000*time);
	
		subnotes = lengths[i].split("-");
		for (s in subnotes)
		{
			var noteToPlay = MIDI.keyToNote[notes[i]];
			if (subnotes[s] == 'sr' || subnotes[s] == 'er' || subnotes[s] == 'qr' || subnotes[s] == 'hr' || subnotes[s] == 'wr')
				noteToPlay = 0;
			
			time += (lengthMap[subnotes[s]]);
			
			MIDI.noteOn(0, noteToPlay, 127, time);
		}
		playingNote = 0;
	}
	
	setTimeout(function() {
		$(elements).animate({opacity: 1});
	}, 1000*(time + 2));
};

var removeNote = function(noteElement)
{
	$(noteElement).remove();
	var sizeSoFar = 50;
	$('.added-note').each(function() {
		$(this).animate({left: sizeSoFar});
		sizeSoFar += parseInt($(this).css('width').replace('px', ''));
	})
};

(function() {
	// disable mobile safari "bounce"
	//document.addEventListener('touchmove', function(e){ e.preventDefault(); }, false);

	// REMOVE BLANK CHARS FROM BEGINNING AND END OF STRING
	String.prototype.trim = function () {
		return this.replace(/^\s*(\S*(\s+\S+)*)\s*$/, "$1");
	};

	var MoveMyMusic = function() {
		var SELF = this,
			SPEED,
			SPACING,
			PATTERN = [], // PATTERN TO PLAY
			LISTEN = true, // LINK EACH COLOR TO A NOTE
			RESPONSE = []; // USER PLAYBACK

		this.init = function() {
			SELF.setDefault();
			$('a').click(function() {
				var playNote = $(this).data('note');
				if (typeof(playNote) == "string")
					playNote = MIDI.keyToNote[playNote];
				SELF.inputSingle(playNote);
			})
		}

		this.setDefault = function() { // set default values
			LISTEN = true;
			PATTERN = [];
			RESPONSE = [];
			SPACING = 360;
			SPEED = 250;
		}
		
		this.inputSingle = function(note) {
			if(LISTEN === true ) { 
				SELF.playSingle(note);
			} 
		}

		this.playSingle = function (note) { // play a color/note
			MIDI.noteOn(0, note, 127, 0);
			setTimeout(function() { // turn off color
				MIDI.noteOff(0, note, 0);
			}, SPEED);
		}
	}

	MIDI.loadPlugin({
		soundfontUrl: "js/soundfont/",
		instrument: "acoustic_grand_piano",
		callback: function() {
			Mmm = new MoveMyMusic;
			Mmm.init();
			MIDI.loader.stop();
			$('.loader').remove();
		}
	});
	
	Event.add("body", "ready", function() {
		MIDI.loader = new widgets.Loader("Loading MoveMyMusic");
	});
	
	startPos = $('#section-notes .col-sm-10').position();
	
	var attachDrag = function()
	{
		$('.note').draggable({
			helper: 'clone',
			start: function() {
			},
			drag: function() {
				var notes   = $('.' + this.className.split(" ")[0]);
				var foundNote;
				for (i = 0; i < notes.length; i++)
				{
					if (!$(notes[i]).hasClass('added-note'))
					{
						foundNote = notes[i]
					}
				}
				
				var theNote     = $(foundNote).clone();
				var top         = parseInt($(theNote).css('top').replace('px', ''));
				var comb        = parseInt((325 - (startPos.top + top)) / 20);
				var currentNote = notesOrder[comb % 7];
				if (currentNote && $(foundNote)[0].className.indexOf('rest') == -1)
				{
					var imageParts  = $($('.' + this.className.split(" ")[0])[0]).css('background-image').split(".");
					imageParts[imageParts.length - 1] = '-' + currentNote.toLowerCase() + '.png)';
					$(foundNote).css('background-image', imageParts[0] + "." + imageParts[1] + imageParts[2]);
				}

			},
			stop: function()
			{
				var notes   = $('.' + this.className.split(" ")[0]);
				var foundNote;
				for (i = 0; i < notes.length; i++)
				{
					if (!$(notes[i]).hasClass('added-note'))
					{
						foundNote = notes[i]
					}
				}
				
				var newPos = 50;
				$('.added-note').each(function(el) {
					newPos += parseInt($(this).css('width').replace('px', ''));
				});
				
				var theNote  = $(foundNote).clone().addClass('added-note').animate({left: newPos});
				var top      = parseInt($(theNote).css('top').replace('px', ''));
				var comb     = parseInt((345 - (startPos.top + top)) / 20);
				var nnumber  = parseInt(4 + ((comb) / 7));
				var fullNote = notesOrder[comb % 7] + nnumber;
				$(theNote).click(function() {
					removeNote(this);
				})
				if ($(theNote)[0].className.indexOf('rest') == -1)
					MIDI.noteOn(0, MIDI.keyToNote[fullNote], 127, 0);
				else
					$(theNote).animate({top: -200});
				
				if ((startPos.top + top) <= 345 && (startPos.top + top) >= 115)
					$('#section-notes .col-sm-10').append(theNote);
			}
		});
	}
	
	attachDrag();
	
	$('.submitBtn').click(function() {
		playMusic();
	});
	
	$('.clef').click(function() {
		if (confirm("Are you sure you want to change your clef? This will clear all notes."))
		{
			if ($(this).attr('src') == 'img/note/treble-clef.png')
			{
				$(this).attr('src', 'img/note/bass-clef.png');
				$(this).removeClass('treble').addClass('bass');
				notesOrder = bassNotesOrder;
			} else {
				$(this).attr('src', 'img/note/treble-clef.png');
				$(this).removeClass('bass').addClass('treble');
				notesOrder = trebleNotesOrder;
			}
			$('.added-note').each(function() {
				removeNote(this);
			})
		}
	})
	
	
})();