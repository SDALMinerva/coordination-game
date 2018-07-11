function startDiscussIntro() {   
    var intro = introJs();
    intro.setOption('exitOnOverlayClick', false);
    intro.setOption('exitOnEsc', false);
    intro.setOption('showStepNumbers', false);
    intro.setOption('skipLabel', '');
    intro.addSteps([
      {
        element: document.querySelectorAll('#playerDiv')[0],
        intro: "In each round, you will be assigned a randomly chosen <strong>identity (or avatar)</strong> and a <strong>threshold T</strong>. " +
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
               "Here, you will see your friends and their thresholds. " +
               "<br><br>You can <strong>send messages</strong> to your friends.",
      },
      {
        element: document.querySelectorAll('.container-network')[0],
        intro: "This diagram shows <strong>the network</strong> for the round: all of the connections between the players in your group. " +
               "The gray line between two avatars means that they are friends. " +
               "<br><br>You (and everyone else) can observe the connections between players in your group in this box. " +
               "The shape of the network may or may not be the same in each round.",
      },
      {
        element: document.querySelectorAll('.container-groupList')[0],
        intro: "These are all of the players in your group. Some or all of them are in your list of friends. " +
               "When a player moves on to the next page and is waiting for you, it will be displayed here. ",
      },
      {
        element: document.querySelectorAll('.message-tool')[0],
        intro: "In the <strong>messaging part</strong>, you can use this tool to send messages to your friends " +
               "revealing your intention to participate or not in the group event. " +
               "<br><br>You can send: <strong>1) 'I will participate'</strong>, <strong>2) 'I will not participate'</strong> or choose <strong>'no messages</strong> for the round. " +    
               "<br><br>Each player can send a message only to his/her friends. " +
               "No one can see other players’ messages. " +
               "<br><br>Try using the messaging tool by selecting the recipient and a message (from the dropdown menu). " +
               "You will click 'Submit' to send your messages in the actual game.", 
        position: "top",
        disableInteraction: false,
        position: "right",
      },
      {
        element: document.querySelectorAll('.message-card')[0],
        intro: "You will view the messages sent to you by your friends in your inbox. " +
               "The messages from friends will be received and viewed in the <strong>decision part</strong>." 
        //position: "top",
      },
      {
        element: document.querySelectorAll('#stopButton')[0],
        intro: "Once you are done with sending messages, you can click 'Next' to proceed to the decision part. " +
               "You cannot send messages in the decision part.",
        disableInteraction: true,
      },
      {
        element: document.querySelectorAll('#stopModal-content')[0],
        intro: "You can review your messages and click “Edit” to make changes: you can remove existing messages or send new ones. " +
               "Make sure that you send all of the messages you want before clicking 'Continue' as you cannot get back to the messaging part. " +
               "When you click 'Continue', you will proceed to the decision part.",    
        disableInteraction: true,
      },
      {
        element: document.querySelectorAll('.next-button')[0],
        intro: "<h5><em><strong>Please click 'Continue' to move to the tour of the decision part.</strong></em><h5>",
      },
    ]);
    intro.onchange(function(targetElement) {   
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
        element: document.querySelectorAll('.message-card')[0],
        intro: "In the decision part, each player can observe the messages sent to them. " +
               "You will not be able to send or receive any more messages.",
        position: "top",
      },
      {
        element: document.querySelectorAll('#friendsDiv')[0],
        intro: "You can click on your friends' avatars to view the messages between you and them.", 
      }, 
      {
        element: document.querySelectorAll('#participate-group')[0],
        intro: "After reviewing the messages, each player in the group then must decide whether <strong>to participate</strong> or <strong>not " +
               "participate</strong> for this round. After making your participation decision for the round, a new round will start. You will not observe the outcome of the rounds. " +
               "<br><br>After you play all the rounds, we will choose a random round and you will be paid based on the " +
               "result of that round. Because each round has the same chance of being chosen for payment, you should pay careful attention to " +
               "each round.",
      },
      {
        element: document.querySelectorAll('#help-nav')[0],
        intro: "At any time, you can view the instructions, this tour and the quiz.",
        disableInteraction: true,
      },
      {
        element: document.querySelectorAll('.next-button')[0],
        intro: "Next, you will have 3 practice rounds before the actual game starts. <br/><br/><h5><em><strong>Please click 'Continue' now.</strong></em><h5/>",
      },
    ]);
     
    intro.start();
  }
