### I'm just practicing python by making cli toys.

## Brawlstars  
brawlstars.py is the main script that calls the brawlstars api and writes match history to the local sqlite db.
To use this script, you will need to
    - Sign up for an brawlstars API key and create an api_keys.py file
    - import the key into the priamry script and 
    - run the brawl_db.py script to initialize/update the db, or use the existing one
    - call brawlstars.py to fetch and download maps, or set up a schedule / cron job to run it regularly. (Currently the BS api only saves the 25 most recent matches, so an hourly job should prevent anything from getting missed)
 
## gameLearning
It has the spirit of a text adventure but there isn't a lot to it.
run gameLearning.py to play it. or maybe play the cliMon one instead.

# cliMon
A really basic CLI pokemon clone. it's maybe too random to be practical, but it is mostly a game.
run "python cliMon.py" to play the game. Enter names for your PyCliMon (First 3 for player one, last 3 for player two), then use 1, 2, and enter keys to play.
my error handling is currently bad, so don't get cute with your inputs.


# typer
To play, you need to create a csv with two columns, "Words" and "Best Time". the words column should be populated by you.
Validation takes place for the entire column, so you can use whole sentences or single words
##### I've spent the entire day reading through the southern reach trilogy instead of coding. whoops.
