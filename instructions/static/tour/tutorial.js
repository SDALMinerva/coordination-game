function startDiscussIntro() {   
    var intro = introJs();
    intro.setOption('exitOnOverlayClick', false);
    intro.setOption('exitOnEsc', false);
    intro.setOption('showStepNumbers', false);
    intro.setOption('skipLabel', '');
    intro.addSteps([
      {
        element: document.querySelectorAll('#playerDiv')[0],
        intro: "In each round, you will be assigned a randomly chosen identity (or avatar). " +
               "You will also see your threshold, T=3 in this example above, and the summary of the possible earnings. " + 
               "Note that, in each round, everyone will be assigned a new avatar and a new threshold. " +
               "<br\><br\>You can click here to see your own wall and what your friend(s) have posted.",
      },
      {
        element: document.querySelectorAll('#friendsDiv')[0],
        intro: "In each round, you will be connected to some or all of the other people in your group. " + 
               "They will be called <strong>Your friends</strong>. " +
               "You will see the thresholds of your friends on your page. " +
               "You can also see the thresholds of friends of your friends on their pages. " +
               "<br\><br\>In this example, these are all of your friends. " +
               "You can click on them to see their wall and post messages. " +
               "Try clicking on a few to see how the wall changes.",
      }, 
      {
        element: document.querySelectorAll('.message-tool')[0],
        intro: "As mentioned above, your earnings depend on your decision to participate and others’ decisions to participate. " +
               "Before making your participation decision, you will be given an opportunity to post messages on your wall or on your friends’ walls to reveal your intention to participate or not in the group event. " +
               'You have the following two messaging options to post on the walls: 1) "I will participate", 2) "I will not participate". ' +
               "Each player can post a message only on his/her own friends' walls. Posts on a player's wall can be viewed by all of his/her friends." +
               "<br/><br/>" +
               "Select a message and the recipient wall to post to by clicking on the down arrows in each of the input fields. " +
               "You also have the option to send to 'Everyone' which means posting on everyone's wall but your own. " +
               "Once your message options have been selected, click the 'Post Message' button.",
        position: "top",
        disableInteraction: false,
        position: "right",
      },
      {
        element: document.querySelectorAll('.wall-card')[0],
        intro: "You will view the posts on your wall and on your friends' walls in the decision part.",
        //position: "top",
      },
      {
        element: document.querySelectorAll('.container-network')[0],
        intro: network_display + " network represents how people are connected in your group. " +
               "All of the five people in your group will be connected to some or all of the other people in the group, and can view the thresholds of their friends and their friends of friends. " +
               "You (and everyone else) can observe the connections between people in your group in the network box. " +
               "The screen below shows an example of the network you may see in a round; the gray line between two avatars means that they are friends. " +
               "You will also see the list of your friends, and a list of all the players in your group. " +
               "Note that you will be assigned to a new group in each round. " +
               "The shape of the network may or may not be the same in each round.",
      },
      {
        element: document.querySelectorAll('#stopButton')[0],
        intro: "You will then click 'Next' to finalize your posts.",
        disableInteraction: true,
      },
      {
        element: document.querySelectorAll('#stopModal-content')[0],
        intro: "You will have one last chance to review your posts. Click Continue to leave the discussion, or click Edit to make changes to your posts.",
        disableInteraction: true,
      },
      {
        element: document.querySelectorAll('.next-button')[0],
        intro: "<h5><em><strong>Please click Continue now to advance the tour.</strong></em><h5>",
      },
    ]);
    intro.onchange(function(targetElement = false) {   
        if (targetElement.id == 'stopModal-content') 
            { 
                $('#stopModal-content').css('display','inline-block');
            }
        if (targetElement.id == 'stopButton') 
            { 
                $('#stopModal-content').css('display','none');
            }
        });
    intro.start();
  }
  
  
  function startDecideIntro() {   
    var intro = introJs();
    intro.setOption('exitOnOverlayClick', false);
    intro.setOption('exitOnEsc', false);
    intro.setOption('showStepNumbers', false);
    intro.setOption('skipLabel', '');
    intro.addSteps([
      {
        element: document.querySelectorAll('.wall-card')[0],
        intro: "On the next screen, you will be able to view all of the posts from the other players, but you will not be able to send or receive any more posts. Now is your chance to review what your friends have told you before you make a decision below.",
        position: "top",
      },
      {
        element: document.querySelectorAll('#friendsDiv')[0],
        intro: "Click on your friends avatars to view their walls and what is posted on them. ", 
      }, 
      {
        element: document.querySelectorAll('#participate-group')[0],
        intro: "The screen below shows the decision making area. " +
               "In this part, each player can observe the messages posted on their own walls and on their friends’ walls. " +
               "Each person in the group then must decide whether to participate or not participate in the group event for this round. " +
               "After making your participation decision for the round, a new round will start. " +
               "After you play all the rounds, at the end of the experiment, we will choose a random round and you will be paid based on the results of that round. " +
               "Because each round has the same chance of being chosen for payment, you should pay careful attention to each round. ",
      },
      {
        element: document.querySelectorAll('#help-nav')[0],
        intro: "At any time, you can view the instructions, this tour and the quiz.",
      },
      {
        element: document.querySelectorAll('#reward-summary')[0],
        intro: "Here you can see the earnings structure for the game.",
      },
      {
        element: document.querySelectorAll('.next-button')[0],
        intro: "Next, you will take a short quiz, play test rounds, and when you are ready, begin the game. <br/><br/><h5><em><strong>Click 'Next' to continue.</strong></em><h5/>",
      },
    ]);
     
    intro.start();
  }