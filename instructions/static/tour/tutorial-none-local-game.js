  
  function startDecideIntro() {   
    var intro = introJs();
    intro.setOption('exitOnOverlayClick', true);
    intro.setOption('exitOnEsc', true);
    intro.setOption('showStepNumbers', false);
    intro.setOption('skipLabel', '');
    intro.addSteps([
      {
        element: document.querySelectorAll('#playerDiv')[0],
        intro: "In each round, you will be assigned a randomly chosen <strong>identity (or avatar)</strong> and a <strong>threshold T</strong>." +
               "In this example above, your avatar is <strong>Cow</strong> and your <strong>threshold T=1</strong>. " +
               "<br><br>In each round, every player will be assigned a new avatar and a new threshold.",
      },
      {
        element: document.querySelectorAll('#reward-summary')[0],
        intro: "Here you can see the possible earnings for the round.",
      },
      {
        element: document.querySelectorAll('#friendsDiv')[0],
        intro: "In each round, you will be connected to some or all of the other players in your group. They will be called <strong>your friends</strong>. " +
               "Here, you will see your friends and their thresholds.",
      },
      {
        element: document.querySelectorAll('.container-network')[0],
        intro: "This diagram shows <strong>your network</strong> for the round: your connections (friends) in the group. " +
               "There is a gray line between your avatar and each of your friends' avatars. " +
               "<br><br>You can observe your connections in this box, but you cannot observe the connections between your friends or other players. " +
               "The shape of the network may or may not be the same in each round.",
      },
      {
        element: document.querySelectorAll('.container-groupList')[0],
        intro: "These are all of the players in your group. Some or all of them are in your list of friends. " +
               "When a player moves on to the next page and is waiting for you, it will be displayed here. ",
      }, 
      {
        element: document.querySelectorAll('#participate-group')[0],
        intro: "Each player in the group then must decide whether <strong>to participate or not " +
                "participate</strong> for this round. After making your participation decision for the round, a new round will start. You will not observe the outcome of the rounds. " +
               "<br><br>After you play all the rounds, we will choose a random round and you will be paid based on the " +
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
