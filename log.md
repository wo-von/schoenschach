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
**TODO:**
Just write classes for different ppieces and create a generic board class and draw it. 
afterwards:
- either keyboard or mouse: show where each piece can go.