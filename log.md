# 100 Days Of Code - Log

### Day 0: before 4th Nov 2021

**Progress:** 
- Set up the repository, added (through github) gitignore, and license, updated readme and started the log
- Added examples from these courses and also CS50's artificial intelligence course.
- decide to use pygame instead of tkinter, but might give that a go some other time too if pygame proves not good enough working with pictures, but should be ok.

**Link to work:**

[Project page of the minesweeper project of CS50 artificial intelligence](https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/)

[Problem set 3 of the MIT's 6.002 is what is being considered here](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/assignments/ٰ)

**Thoughts:**  
I started this in July and then quit immediately, which is not the point of 100 days of code. That is why I am calling everything before day 0, and 4th Nov. as day 1. I should stick to the challenge from now on.


### Day 1: 4th Nov. 2021

**Progress:** 
- Based on the Minsweeper example and a [tutorial online](https://dr0id.bitbucket.io/legacy/pygame_tutorial00.html) made the board. It is now properly resized, has a caption. But nothing else

**Thoughts:** 

**TODO:** 
Find a better PNG image file for the board, since it needs to have boundaries so that I can print the coordinates (A..H and 1..8). it might need to later be refactored into a class so that multiple instances of it can be run, since pygame supports only one screen

### Day 2: 5th Nov. 2021
**Progress:** 
Did not work for a full hour, but found better pieces and boards and need to set them up for now. putting image on top of each other also works with no problem
**TODO:**
- seems like I should keep calculating the board size, the paddings, etc. lets find out if pygame can scale automatically nd if not write tests so that the board size etc. has the desired dimensions
- make list of assets. for now: type of chess boards: bauhaus, netflix
- Download better quality chess pieces
- Tomorrow: finish the while asset with board and pieces and make scaling work.


### Day 3: 8th Nov. 2021
**Progress:**
This is not how it should be, you lose a challenge if you do not code for even one day and now I have not code for 2 days, but I am going to cut myself some slack, my laptop at home was not working properly and it was a busy weekend familywise, I also had birthday!
Anyway, today I impelemted a logical representation of a board, still very much incomplete but I think it is nice that I have started to think for myself instead of following the tutorial. Also started using pieces through a class, which is also the correct direction.
**TODO:**
- kepp doing the tutorial, you should know how grapfics works before coupling it to a loogical representation.
- Also represent the board in a class.
- maybe like CS50, use a runner which imports the mosules, that should be nicer

### Day4: 9th Nov. 2021:
**Progress:**
Implemented a very simple and inefficient animation, which might for now work. but soent a lot of time browsing different tutorials. This is what I do, also in my job and specially at the beginning when things are unclear, trying to learn and follow the steps of other prople, and getting lost in learning material. I should avoid this and impelemt the project one step at a time.
use a dict for the paths of the png files of the chess pieces, I have a better picture of how to move forward after the disappoiting first half of day 4.
used black to format the files, but 1 file at a time
**TODO:**
Just write classes for different ppieces and create a generic board class and draw it. 
afterwards:
- either keyboard or mouse: show where each piece can go.

### Day5: 10th Nov. 2021:
**Progress:**
worked on classes of pieces, but forgot to write the log, see Day6
**TODO:**
see Day6

### Day6: 11th Nov. 2021:
**Progress:**
Finished a draft of the classes for pieces which seems to be working for now, I am goning to stay with unless I realize it could get a lot better. Made the board also compatible with this version and it is working now.
**TODO:**
should work on the board, make coordinates and so correct, and draw a board based on the dict (or whatever data structure) that hold the board state.

### Day7/0: 12th Nov. 2021:
**Progress:** Not much, started very late and was distracted
**TODO:** Evetything that should have been done today

### Day7/1: 15th Nov. 2021:
**Note:**
very little to no progress on 13th and 14th. so I have not counted them towards days
**Progress:**
use a Piece object that holds the piece and coordinated in the board list. Maybe the x y for the pieces is unnecessary. generally the data structures need a lot of work, maybe i shold use a dictioary instead. just wanted to rush towards drawing the board, but it does not work
**TODO:**
debug the current code and see why it does not work. Think on how to impelment the whole thing

### Day 8: 16th Nov. 2021:
**Progress:**
Moved the drawing part of the board into the class, works. But I think the code is getting a bit compplicted and I am losing track of the big picture. For that I need to refresh my knowledge of pygame. Also, keep things simple, it is nice that I am trying to do things via paramaeters so that they are scalable later, but the fact is that I have no idea how it is going to be, maybe pygame takes care of scaling itself, because now I am very concerned with scaling the board and translating everythign into scale
**TODO:**
Read a pygame tutorial to get an idea how things are going to be. for now I have [this](https://coderslegacy.com/python/python-pygame-tutorial/) and [this](https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-tutorial-movement/). Also read about resizing and scaling since that is bothering you so much. Also think about the data structures, the current one is working, but is getting complicated

### Day9:16th Nov. 2021:
**Progress:**
No coding today, was literature review day because of reasons that was said yesterday. Read till part 13 of [this](https://www.patternsgameprog.com/series/discover-python-and-patterns/). Should have given it a rest after some time,, since i wanted to keep reading, but was distracted and kept browsing around. But is a very good one and is alreay showing me how to proceed
**TODO:**
keep reading the above mentioned tutorial, maybe start taking notes since it is getting a bit complicated

### Day10:17th Nov. 2021:
**Progress:**
Started seperating differen functionalities, and run the whole game through an object, which should be nice later if different instances are to run. Was generally very distracted, so nothing important was done
**TODO:**
impelemnt the keyboard interaction and maybe highlight the square you are on.

### Day11: 23 Nov. 2021:
**Progress:**
- Add the process input method of the Game object
- The timeline of the 1000 days has been messed up, I am going to count from here (12- 15 are both day 7 and there are 16th Nov for days 8 and 9, the problem is inconsistency, but hope to  stay consistent from here on)
**TODO:**
- Make the game ruubale in the current form
- implement selected square
- impelement legal moves

### Day12: 24 Nov. 2021:
**Progress:**
Everything works as before, but his time in the framework of game development principles, might need to restructure the more that I go forward
**TODO:**
- draw a square for the picked square
- keep going with the tutorial
- write a seperate module for settings, they are kind of bothering, being referenced everywhere

### Day13: 25 Nov. 2021:
Writing this on 26th Nov, but the progress was done on the day it was supposed to
**Progress:**
simply draw a square where, and randomly so, not even pointing to a specific square

### Day 14: 26. Nov. 2021:
**Progress:**
- used property for the first time in my life, was simple and  fun! (not sure why I was so confused about it when I first read about it, maybe the connection with wrapper, decorator, etc.)
- now draw the square properly, and in the system of the game design pattern, but does not work properly, the screen keeps blinking which is probably because of the constant drawinf onto it, also the key press has no effect
**TODO:**
make the keys work

### Day 15: 27. Nov. 2021:
**Progress:**
Very lazy day, just debugged the code, saw that the keyboard input is actually working and tried to fix it. it is responsive, but with a funny bug, so not all the board is printed, i am not sure why. Also built a delay, it is not very demanding anymmore, but is not also the best solution, best maybe to render the parts that habe been changed

### Day16: 29. Nov 2021:
**Progress:**
- Implemented the allowed moves of all the pieces. In current implementation, they simplay send back when they can go and then later in the Game or Board I am going to decide which ones are suitable for the current state of the game.
- works on lenovo, but probablyy not on xps, since it was buggy the other day and not much has changes in the impelmentation of drawing the while board, should be checked there later too
- Almost took the whole day for this, and it was kidn of a procrastination from other stuff, should work more focused and in limited time, the point is to work an hour only to be better focused.
**TODO:**
- Check the codde on xps to see why it was being drawn incorrectly there
- draw only the parts that are changed
- draw circles for possible moves
- make a move visible finaly!

### Day17: 30 Nov. 2021:
**Progress:**
- started implementing the possible moves, was very distracted and almost did nothing
**TODO:**
- keep implementing the possible moves method

### Day 18: 1 Dec. 2021:
**Progress:**
- draw the possible moves of a single piece on a test board, very raw
**TODO:**
- Draw the possible moves when the piece is picked
- test different pieces
- draw more than one piece and see their connection (hard!)
**Ideas:**
-  