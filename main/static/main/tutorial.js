function startIntro() {   
    var intro = introJs();
    intro.setOption('exitOnOverlayClick', false);
    intro.addSteps([
      {
        element: document.querySelectorAll('#playerLabel')[0],
        intro: "This is your profile. Click here to see your own wall and what your friend(s) have posted.",
      },
      {
        element: document.querySelectorAll('#playerList')[0],
        intro: "These are all of your friends. Click on them to see their wall and post messages. Try clicking on a few to see how the wall changes."
      }, 
      {
        element: document.querySelectorAll('#container-messages')[0],
        intro: "Post messages to the current wall by clicking on the down arrow. You can select any of the messages that are listed. Once selected, click the 'post message' button.",
        position: "top",
      },
      {
        element: document.querySelectorAll('.card')[0],
        intro: "Messages that you post will appear here, but they won't be visible until you move to the next screen. Until then you can delete any messages by clicking on the trash icon.",
        position: "top",
      },
      {
        element: document.querySelectorAll('#mynetwork')[0],
        intro: "Here, you can see your friend connections.",
      },
      {
        element: document.querySelectorAll('.otree-btn-next')[0],
        intro: "When finished posting messages, click next to continue.",
        disableInteraction: true,
      },
      {
        element: document.querySelectorAll('.card')[0],
        intro: "On the next screen, you will be able to view all of the messages from the other players, but you will not be able to send or receive any more messages. Now is your chance to review what your friends have told you before you make a decision below.",
        position: "top",
      },
      {
        element: document.querySelectorAll('#participate-group')[0],
        intro: "At the bottom of the page you will then choose whether or not you want to participate.",
      },
      {
        element: document.querySelectorAll('.otree-btn-next')[0],
        intro: "Click next to exit the tour and continue to the game.",
      },
    ]);
    
    intro.onchange(function(targetElement) { 
        console.log(document.querySelectorAll('.control-label')[0]);  
        if (targetElement.nodeName == 'BUTTON') 
            { 
                $('#participate-group').css('visibility', 'hidden');
            }
        if (targetElement.id == 'participate-group') 
            { 
                $('#participate-group').css('visibility', 'visible');
            }
        });
     
    intro.start();
  }