# CS460botnet

P2P botnet
Running the botnet:
Run multiserv.py in one terminal and bot_1.py in other terminals.
Running the click spam code requires pip install python-uinput.

Our bot creates a new thread at the server terminal for each bot.
This way we could parse inputs from the bots to create additional commands, learn from the information our bots are gathering.

In our latest commit, our bot will be assigned a command to work on when it is initialised and the server will then listen for new bot connections. This network could be used for a DDoS or spamming clicks, keyboard clicks.	

More than our actual implementation, our research on botnets during the project was more rewarding. We learnt about multiple bot network implementations through IRC, using Tor and the simple p2p botnet.

Issues encountered:
We had issues with dynamically creating bots and assigning them at first. We were able to get a workaround for this in an earlier commit (53c12ab), by allotting a designated amount of time to a known amount of ports. This had serious drawbacks since each bot would now block the socket for x amount of time, and the number of bots had to be predetermined.

We fixed this problem by dynamically assigning the port numbers for each bot. As opposed to each bot hogging the socket for a certain amount of time, and having a known number of bots we can now assign each bot that connects to the command and control center (multiserv) their own thread information for each socket. This information is then stored in an array that increments for each new bot that connects.
