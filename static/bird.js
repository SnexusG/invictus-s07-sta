var messages = [], //array that hold the record of each string in chat
  lastUserMessage = "", //keeps track of the most recent input string from the user
  botMessage = "", //var keeps track of what the chatbot is going to say
  botName = 'Chatbot', //name of the chatbot
  talking = true; //when false the speach function doesn't work

function chatbotResponse() {
  talking = true;
  botMessage = "I'm confused"; //the default message

  if (lastUserMessage === 'hi' || lastUserMessage =='hello') {
    const hi = ['hi','hello']
    botMessage = hi[Math.floor(Math.random()*(hi.length))];;
  }

  if (lastUserMessage === 'name') {
    botMessage = 'My name is chat bot';
  }

  if(lastUserMessage.toLowerCase() == `period cramps` || lastUserMessage.toLowerCase() == `i have period cramps` || lastUserMessage.toLowerCase() == `i have menstruation cramps`){
    botMessage = `Period cramps can cause hrobbing or cramping pain in your lower abdomen that can be intense. Menstrual cramps are very common: In Clue, 
    about 3 in 4 people report experiencing cramps just before or during their period. Would you like to know about self care for period cramps?`
}

  if(lastUserMessage.toLocaleLowerCase() == `yes`){
    botMessage = `Taking pain medication such as ibuprofen or paracetamol may help to relieve menstrual cramps and pain. Using a heating pad may also help.`
  }
    
    if(lastUserMessage.toLowerCase() == "pcos" || lastUserMessage.toLowerCase() == "polycystic ovary syndrome" || lastUserMessage.toLowerCase() == "i have polycystic ovary syndrome"){
        botMessage = `List of Things You can Eat to reverse PCOS
        Consume healthy carbs like whole grains, legumes, flax seeds, sweet potatoes, nuts, etc.
        Boost your daily fibre intake by adding broccoli, beans, spinach, berries, etc.
        Make a high-protein diet plan and follow it strictly. It would help if you tried greek yoghurt and sesame seeds too.
        Healthy fats are also helpful to the PCOS cure at home. You can start cooking your meals in coconut or olive oil.
        Consume antioxidants by eating a lot of fruits like avocados and dry fruits.`
    }




}

function newEntry() {
  if (document.getElementById("chatbox").value != "") {
    lastUserMessage = document.getElementById("chatbox").value;
    document.getElementById("chatbox").value = "";
    messages.push(lastUserMessage);
    chatbotResponse();
    messages.push("<b>" + botName + ":</b> " + botMessage);
    Speech(botMessage);
    for (var i = 1; i < 8; i++) {
      if (messages[messages.length - i])
        document.getElementById("chatlog" + i).innerHTML = messages[messages.length - i];
    }
  }
}

function Speech(say) {
  if ('speechSynthesis' in window && talking) {
    var utterance = new SpeechSynthesisUtterance(say);
    //msg.voice = voices[10]; // Note: some voices don't support altering params
    //msg.voiceURI = 'native';
    //utterance.volume = 1; // 0 to 1
    //utterance.rate = 0.1; // 0.1 to 10
    //utterance.pitch = 1; //0 to 2
    //utterance.text = 'Hello World';
    //utterance.lang = 'en-US';
    speechSynthesis.speak(utterance);
  }
}

document.onkeypress = keyPress;
function keyPress(e) {
  var x = e || window.event;
  var key = (x.keyCode || x.which);
  if (key == 13 || key == 3) {
    newEntry();
  }
  if (key == 38) {
    console.log('hi')
  }
}

function placeHolder() {
  document.getElementById("chatbox").placeholder = "";
}