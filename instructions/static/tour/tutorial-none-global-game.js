function startDecideIntro() {   
    var intro = introJs();
    intro.setOption('exitOnOverlayClick', true);
    intro.setOption('exitOnEsc', true);
    intro.setOption('showStepNumbers', false);
    intro.setOption('skipLabel', '');
    intro.addSteps([
      {
        element: document.querySelectorAll('#playerDiv')[0],
        intro: "In each round, you will be assigned a randomly chosen <strong>identity (or avatar)</strong> and a <strong>threshold T</strong>. " +
               "In this example above, your avatar is <strong>Cow</strong> and your <strong>threshold T=1</strong>. " +
               "In each round, everyone will be assigned a new avatar and a new threshold.",
      },
      {
        element: document.querySelectorAll('#reward-summary')[0],
        intro: "Here you can see the possible earnings for the round.",
      },
      {
        element: document.querySelectorAll('#friendsDiv')[0],
        intro: "In each round, you will be connected to some or all of the other players in your group. " +
               "They will be called 'your friends', and will be listed in this box. You will also see the thresholds of your friends here. ",
      },
      {
        element: document.querySelectorAll('.container-network')[0],
        intro: "The network represents how players are connected in your group in a round. " +
               "The gray line between two avatars means that they are friends. " +
               "All of the 5 players in your group will be connected to some or all of the other players in the group. " + 
               "You (and everyone else) can observe the connections between players in your group in ‘The Network’ box. " +
               "Note that you will be assigned to a new group in each round. The shape of the network may or may not be the same in each round.",
      },
      {
        element: document.querySelectorAll('.container-groupList')[0],
        intro: "These are all of the players in your group. Some or all of them are in your list of friends." +
               "When a player moves on to the next page and is waiting for you, it will be displayed here.  ",
      }, 
      {
        element: document.querySelectorAll('#participate-group')[0],
        intro: "Each person in the group must decide whether to participate or not " +
               "participate in the group event for this round. After making your participation decision for the round, a new round will start. You will not observe the outcome of the rounds." +
               "After you play all the rounds, at the end of the experiment, we will choose a random round and you will be paid based on the " +
               "results of that round. Because each round has the same chance of being chosen for payment, you should pay careful attention to " +
               "each round.",
      },
      /*{
        element: document.querySelectorAll('#help-nav')[0],
        intro: "At any time, you can view the instructions, this tour and the quiz.",
        disableInteraction: true,
      },
      {
        element: document.querySelectorAll('.next-button')[0],
        intro: "Next, you will practice with test rounds, and when you are ready, begin the game. <br/><br/><h5><em><strong>Please click 'Continue' now.</strong></em><h5/>",
      },*/
    ]);
     
    intro.start();
  }
  
  
  
