stretch club
==========================
### Requirements ###
* list of stretches
* directions of stretch
    * accompanying images or gifs on how to do the stretch (steps?)
* timer for stretch duration
* randomization of stretches
* organized by muscle group

### Endpoints ###

/stretches
	 Shows full list of stretches
/stretches/routine
	 Randomly generated routine for stretches
/stretches/<ID>
	 Shows details of stretch
		 Instructions
		 Muscle groups targeted

## Product Goal ##
* I want to have the ability to generate a routine full of stretches. 
* I want to have the ability to create, edit, save a 'playlist'
* when I play the stretches of the day, it should iterate through the list. Per stretch, it should:
	* give instructions, 
	* after 5 seconds start a 10 second timer to execute
	* go to the next stretch
	* repeat above
* I should have the ability to pause, restart, go back, go next.
* I want to add, remove, and edit stretches
* I want to have the ability to save routines and name them
* I want to schedule routines
* I want to be able to edit the recommended timers
