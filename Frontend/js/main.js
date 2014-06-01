var Mmm, MIDI;
(function() { "use strict";
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
			/*Event.add($('a')[0], 'mousedown', function(event) {
				console.log($(event.target).data('note'));
				SELF.inputSingle(80);
			});*/
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
		}
	});
	
	Event.add("body", "ready", function() {
		MIDI.loader = new widgets.Loader("Loading MoveMyMusic");
	});
	
	$('.q-note').draggable({
			helper: 'clone',
			grid: [ 27, 27 ],
			start: function() {
			},
			drag: function() {
				var notes = $('.q-note');
				console.log($(notes[notes.length - 1]).css('top'));
			},
			stop: function()
			{
				var notes   = $('.q-note');
				var theNote = $(notes[notes.length - 1]).clone().addClass('added-note').animate({left: (120 + ($('.added-note').length * 90))});
				var top    = parseInt($(theNote).css('top').replace('px', ''));
				console.log(top);
				if (top <= 221 && top >= -80)
					$('#section-notes .row').append(theNote);
			}
		});
})();