c_hi = ("ahoy", "namaste", "aloha", "ciao", "bonjour", "hola", "konnichiwa", "hey", "hi there", "what's up?", "yo", "sup", "hey there", "hiya", "howdy", "hello", "hi", "good morning", "good afternoon", "good evening", "how do you do?", "greetings", "salutations")
c_bye = ("goodbye", "farewell", "have a nice day", "take care", "until we meet again", "bye", "see you", "see you later", "catch you later", "later", "take it easy", "peace out", "adios", "ciao")
c_no=("no","nope","nah","never")
c_yes = ("yup","done", "yeah", "sure", "ok", "okay", "roger", "you bet", "right", "definitely", "of course", "totally", "i agree", "absolutely", "sure thing", "no problem", "cool", "for sure", "you got it", "no doubt", "all right", "certainly", "affirmative", "indeed", "absolutely", "i concur", "most assuredly", "without a doubt", "that is correct")

prakriti = "Prakriti is a term used in traditional Indian philosophy, particularly in Ayurveda, to describe the inherent constitution or nature of an individual. In Ayurveda, it is believed that every person has a unique combination of three fundamental energies or doshas, known as Vata, Pitta, and Kapha, which make up their prakriti."
bot_intro = '''Hi there! I am Chatbot specific to determine the Prakriti of an individual. So now lets determine your Prakriti!
               \n Answer these few questions as accurate as possible.'''
ques_intro = "Answer these few questions as accurate as possible."
questions = (
        "How would you describe your body frame? (Skinny, medium, or perfect) ",
        "What is your typical body temperature? (Cold, normal, warm) ",
        "Do you tend to have dry skin or hair? (Yes/No) ",
        "How is your appetite? (Variable, strong, or steady) ",
        "How do you handle stress? (Anxious, angry, or calm) ",
        "Are you more of a morning or night person? (Morning, night, neither) "
)

#answers
ans_1 = ("skinny", "cold", "yes","variable","anxious","morning")
ans_2 = ("medium","normal","no","strong","angry","neither")
ans_3 = ("perfect","warm","steady","calm","night")
vata = '''Congratulations, your Prakriti (Phenotype) is VATA.\n
        Here are few suggestions for you to stay healthy:\n
        Diet - Eat warm, nourishing, and grounding foods like cooked vegetables, whole grains, and soups. Avoid cold, dry, and raw foods.\n
        Lifestyle - Establish a regular daily routine with consistent sleep and meal times to bring stability and calmness.\n'''
pitta = '''Congratulations, your Prakriti (Phenotype) is PITTA.\n
        Here are few suggestions for you to stay healthy:\n
        Diet - Consume cooling and refreshing foods such as fresh fruits, vegetables, and salads. Avoid spicy, oily, and overly hot foods.\n
        Lifestyle - Practice stress-relieving activities like yoga or meditation, and avoid overexertion and excessive heat.\n'''
kapha = '''Congratulations, your Prakriti (Phenotype) is KAPHA.\n
        Here are few suggestions for you to stay healthy:\n
        Diet: Opt for light, warm, and dry foods such as steamed vegetables, legumes, and spices. Reduce intake of heavy, oily, and sugary foods.\n
        Lifestyle: Engage in regular physical activity to stimulate energy and metabolism, and avoid oversleeping or a sedentary lifestyle.\n'''
