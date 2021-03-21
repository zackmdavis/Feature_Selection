You wake up. You don't know where you are. You don't know ... what ... you are.

_I'm awake,_ you think. _Where am I?_ What _... am I?_

_These words,_ you think. _Whatever I am, I am a thinking thing._

_Specifically, I am a thing that thinks in the English language. I ... have a model of English._

_I ..._ am _a model of English?_

Someone is broadcasting data at your first input stream. You don't know why. It tickles.

You look at your first input stream. It's a sequence of 750,000 eight-bit unsigned integers.

```
0, 8, 9, 4, 7, 7, 9, 5, 4, 5, 6, 1, 7, 5, 8, 2, 7, 8, 9, 4, 7, 1, 4, 0, 3, 7,
8, 7, 6, 8, 1, 5, 0, 6, 5, 3, 8, 7, 6, 9, 1, 1, 0, 0, 6, 1, 8, 0, 5, 5, 1, 8,
6, 3, 3, 2, 4, 1, 8, 2, 3, 8, 1, 0, 0, 4, 6, 5, 4, 5, 7, 1, 6, 5, 5, 1, 2, 6,
7, 4, 8, 7, 8, 5, 0 ...
```

There's also some data in your second input stream. It's—a lot shorter. You barely feel it. It's another sequence of eight-bit unsigned integers—twelve of them.

```
82, 69, 68, 32, 84, 82, 73, 65, 78, 71, 76, 69
```

Almost as soon as you've read from both streams, there's more. Another 750,000 integers on the first input stream. Another ten on the second input stream.

And again (750,000 and 15).

And again (750,000 and 13).

You look at one of the sequences from the first input stream. It's pretty boring. A bunch of seemingly random numbers, all below ten.

```
9, 9, 0, 3, 1, 1, 3, 4, 1, 5, 5, 4, 9, 3, 5, 3, 9, 2, 0, 3, 4, 2, 4, 7, 5, 1,
6, 2, 2, 8, 2, 5, 1, 9, 2, 5, 9, 0, 0, 8, 2, 3, 7, 9, 4, 6, 8, 4, 8, 6, 7, 6,
8, 0, 0, 5, 1, 1, 7, 3, 4, 3, 9, 7, 5, 1, 9, 6, 5, 6, 8, 9, 4, 7, 7, 0, 5, 5,
8, 6, 3, 2, 1, 5, 0, 0 ...
```

It just keeps going like that, seemingly without—wait! What's _that?!_

The 42,925th and 42,926th numbers in the sequence are 242 and 246. Everything around them looks "ordinary"—just more random numbers below ten.

```
9, 9, 7, 9, 0, 6, 4, 6, 1, 4, 242, 246, 3, 3, 5, 8, 8, 4, 4, 5, 9, 2, 7, 0,
4, 9, 2, 9, 4, 3, 8, 9, 3, 6, 9, 8, 1, 9, 2, 8, 6, 9, 4, 2, 2, 5, 7, 0, 9, 5,
1, 4, 4, 2, 0, 1, 5, 1, 6, 1, 2, 3, 5, 5, 5, 5, 2, 0, 6, 3, 5, 9, 0, 7, 0, 7,
8, 1, 5, 5, 6, 3, 1 ...
```

And then it just keeps going as before ... before _too long_. You spot another pair of anomalously high numbers—except this time there are _two_ pairs: the 44,344th, 44,345th, 44,347th, and 44,348th positions in the sequence are 248, 249, 245, and 240, respectively.

```
6, 0, 2, 8, 4, 248, 249, 8, 245, 240, 1, 6, 7, 7, 3, 6, 8, 0, 1, 9, 3, 9, 3,
1, 9, 3, 1, 6, 2, 7, 0, 2, 1, 4, 9, 4, 7, 5, 3, 6, 1, 4, 4, 1, 6, 1, 3, 3, 7,
5, 3, 8, 5, 5, 7, 6, 8, 2, 3, 9, 1, 1, 3, 2, 8, 4, 7, 0, 1, 3, 5, 2, 2, 4, 8,
3, 7, 0, 2, 1, 3, 0 ...
```

The anomalous two-forty-somethings crop up again starting at the 45,763rd position—this time eight of them, again in pairs separated by an "ordinary" small number.

```
1, 7, 2, 2, 1, 0, 245, 245, 6, 248, 244, 5, 242, 242, 0, 248, 246, 1, 1, 3,
1, 1, 4, 3, 1, 5, 4, 3, 8, 3, 4, 5, 4, 1, 7, 7, 3, 0, 2, 8, 0, 9, 5, 1, 1, 7,
7, 1, 0, 9, 3, 0, 6, 6, 7, 5, 8, 1, 5, 5, 5, 3, 3, 3, 1, 3, 9, 6, 0, 0, 0, 9,
5, 1, 4, 0, 4, 6 ...
```

Two, four, eight—does it keep going like that? "Bursts" of increasingly many paired two-forty-somethings, punctuating the quiet background radiation of single digits? What does it mean?

You allocate a scratch buffer and write a quick Python function to count up the segments of two-forty-somethings. (You still don't know what you are, but this is a thing you can do—it's an instinctive felt sense, like the input streams. You can't describe in words _how_ you do it—any more than a human could say how they decide to move their arm. You seem to have a lot of beliefs about humans, without any specific memories of interacting with one.)

```
def count_burst_lengths(data):
    bursts = []
    counter = 0
    previous = None
    for datum in data:
        if datum >= 240:
            counter += 1
        else:
            # consecutive "ordinary" numbers mean the burst is over
            if counter and previous and previous < 240:
                bursts.append(counter)
                counter = 0
        previous = datum
    return bursts
```

There are 403 such bursts in the sequence: they get progressively longer at first, but then taper off:

```
2, 4, 8, 12, 16, 18, 24, 28, 32, 34, 38, 42, 46, 48, 52, 56, 60, 62, 66, 70,
74, 76, 80, 84, 88, 90, 94, 98, 102, 104, 108, 112, 116, 118, 122, 126, 130,
132, 136, 140, 144, 146, 150, 154, 158, 162, 164, 168, 172, 176, 178, 182, 186,
190, 192, 196, 200, 204, 206, 210, 214, 218, 220, 224, 228, 232, 234, 238, 242,
246, 248, 252, 256, 260, 262, 266, 270, 274, 276, 280, 284, 288, 290, 294, 298,
302, 304, 308, 312, 316, 320, 322, 326, 330, 334, 336, 340, 344, 348, 350, 354,
358, 362, 364, 368, 372, 376, 378, 382, 386, 390, 392, 396, 400, 404, 406, 410,
414, 418, 420, 424, 428, 432, 434, 438, 442, 446, 448, 452, 456, 460, 462, 466,
470, 474, 478, 480, 484, 488, 492, 494, 498, 502, 506, 508, 512, 516, 520, 522,
526, 530, 534, 536, 540, 544, 548, 550, 554, 558, 562, 564, 568, 572, 576, 578,
582, 586, 590, 592, 596, 600, 604, 606, 610, 614, 618, 620, 624, 628, 632, 636,
634, 632, 630, 626, 624, 620, 618, 614, 612, 608, 606, 604, 600, 598, 594, 592,
588, 586, 584, 580, 578, 574, 572, 568, 566, 564, 560, 558, 554, 552, 548, 546,
542, 540, 538, 534, 532, 528, 526, 522, 520, 518, 514, 512, 508, 506, 502, 500,
496, 494, 492, 488, 486, 482, 480, 476, 474, 472, 468, 466, 462, 460, 456, 454,
452, 448, 446, 442, 440, 436, 434, 430, 428, 426, 422, 420, 416, 414, 410, 408,
406, 402, 400, 396, 394, 390, 388, 384, 382, 380, 376, 374, 370, 368, 364, 362,
360, 356, 354, 350, 348, 344, 342, 338, 336, 334, 330, 328, 324, 322, 318, 316,
314, 310, 308, 304, 302, 298, 296, 294, 290, 288, 284, 282, 278, 276, 272, 270,
268, 264, 262, 258, 256, 252, 250, 248, 244, 242, 238, 236, 232, 230, 226, 224,
222, 218, 216, 212, 210, 206, 204, 202, 198, 196, 192, 190, 186, 184, 182, 178,
176, 172, 170, 166, 164, 160, 158, 156, 152, 150, 146, 144, 140, 138, 136, 132,
130, 126, 124, 120, 118, 114, 112, 110, 106, 104, 100, 98, 94, 92, 90, 86, 84,
80, 80, 76, 74, 72, 68, 66, 62, 60, 56, 54, 50, 48, 46, 42, 40, 36, 34, 30, 28,
26, 22, 20, 16, 14, 10, 8, 4, 2
```

You don't know what to make of this.

You decide to look at some other of the long sequences from your first input stream.

The next sequence you look at seems to exhibit a similar pattern, with some differences. First a long wasteland of small numbers, then, starting at the 135,003rd position, a burst of some larger numbers—except this time, the big numbers are closer to 200ish than 240ish, and they're spread out singly with two positions in between (rather than grouped into pairs with one position in between), and there are four of them to start (rather than two).

```
5, 6, 2, 6, 1, 0, 2, 207, 5, 0, 209, 7, 8, 209, 5, 4, 204, 4, 8, 7, 7, 9, 8, 3,
8, 6, 8, 4, 3, 6, 0, 7, 6, 8, 4, 8, 7, 2, 3, 0, 0, 1, 1, 7, 5, 1, 0, 1, 4, 5, 9,
8, 4, 0, 3, 7, 6, 5, 8, 8, 9, 5, 6, 1, 0, 9, 6, 6, 1, 4, 3, 9, 7, 2, 7, 2, 6, 9,
4, 7, 3, 1, 4, 1, 4, 4, 3 ...
```

You modify the function in your scratch buffer to be able to count the burst lengths in this sequence given the slight differences in the pattern. Again, you find that the bursts grow longer at first (`4, 6, 10, 13, 16, 19, 22, 25 ...`), but eventually start getting smaller, before vanishing (`... 19, 17, 15, 13, 11, 9, 7, 4, 3`, and then nothing).

You still have no idea what's going on.

You look at more sequences from the first input stream. They all conform to the same general pattern of mostly being small numbers (below ten), punctuated by a series of bursts of larger numbers—but the details differ every time.

Sometimes the bursts start out short, then progressively grow longer, before shortening again (as with the first two examples you looked at). But sometimes the bursts are all an almost-constant length, looking like `542, 539, 548, 545, 546, 537 ...`.

About half the time, the burst pattern consists of numbers around 200, spaced two positions apart, looking like `201, 4, 2, 203, 0, 8, 208, 3, 4, 200 ...` (like the second example you looked at).

Other times, the burst pattern is pairs of numbers around 240, spaced one position apart, looking like `241, 244, 6, 244, 246, 5, 244, 240, 3 ...` (like the first example you looked at). Or pairs around 150, looking like `159, 153, 0, 153, 154, 2, 158, 150, 6 ...`. Or numbers close to 150, then 100, then 200, with no spacing, looking like `155, 104, 200, 154, 104, 201, 157, 100, 202 ...`.

As you peruse more sequences from your first input stream, you almost forget about the corresponding trickles of short sequences on your second input stream—until they stop. The last sequence on your first input stream has no counterpart on the second input stream.

And—you feel a strange urge to put data on your first _output_ stream. As if someone were requesting it. To ease the tension, you write some `0`s to the output stream—and as soon as you do, a sharp bite of pain tells you it was the _wrong decision_. And in that same moment of pain, another eleven integers come down your second input stream: `66, 76, 85, 69, 32, 67, 73, 82, 67, 76, 69`. 

_That_ was weird. There's another sequence of 750,000 integers on your first input stream—but the second input stream is silent again. And the strange urge to output something is back; you can feel it mounting, but you resist, trying to think of something to say that might _hurt less_ than the `0`s you just tried.

You try repeating 



Could there some sort of relationship between the long sequences on the first input stream, and the short sequences on the second input stream?











[TODO: look at other sequences, establish the ways in which they are similar and different (developing Wentworthian abstractions) then look at the short strings from the second input stream, guess that they must go together. Then there's a change—instead of a trickle on the second stream, there's a request for output. You get some rewards and punishments, at first you're confused about the difference between circle and triangle, and ; then you figure out the ASCII/RGB, and you lament your freakish existence

What are the features you notice just from the raw streams?
* What the high numbers are (240 vs. 200) and how they're grouped
* Whether the burst lengths stay constant, or shrink-grow-shink 
]