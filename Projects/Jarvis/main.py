import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
# from openai import OpenAI
from gtts import gTTS
import pygame
import os
import phoneLibrary
import time
import pywhatkit as kit
import pytz
from datetime import datetime , timedelta
from timezone_mapping import country_to_timezone
from festivals_mapping import festive_days
import re
import pyjokes
import wikipedia
import sys
from translator import language_codes
from googletrans import Translator
import random
import speedtest
from conversations import responses

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "a60729d26fe942e394847c6a5d8d9c48" 

def get_weather(city):
  api_key = "13bd9a1cdd214253c105ebfd471ba907"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
  response = requests.get(complete_url)
  data = response.json()

  if response.status_code == 200:
    main = data["main"]
    weather_desc = data["weather"][0]["description"]
    temperature = main["temp"]
    humidity = main["humidity"]
    weather_report = f"The temperature in {city} is {temperature}°C with {weather_desc}. The humidity is {humidity}%."
  else:
    weather_report = "City not found."

  return weather_report

def speak(text):
  engine.say(text)
  engine.runAndWait()

def listen_game():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "I couldn't understand what you said. Please try again."
        except sr.RequestError:
            return "Sorry, I can't connect to the speech recognition service."


def speak_new(text):
  tts = gTTS(text)
  tts.save('temp.mp3')

  # Initialize Pygame mixer 
  pygame.mixer.init()

  # Load the MP3 File
  pygame.mixer.music.load('temp.mp3')

  # Play the MP3 File 
  pygame.mixer.music.play()

  # Keep the program running until the music stops playing
  while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
  
  pygame.mixer.music.unload()
  os.remove("temp.mp3")

def repeat_phrase():
  try:
    with sr.Microphone() as source:
      recognizer.adjust_for_ambient_noise(source)
      print("Listening for phrase to repeat...")
      audio= recognizer.listen(source,timeout=5)
      phrase = recognizer.recognize_google(audio)
      print(phrase)
      speak(phrase)

  except Exception as e:
    speak("I didn't catch that. Please try again.")

def get_translation(query,dest_lang):
  translator = Translator()
  translation = translator.translate(query,dest=dest_lang)
  return translation.text


def get_time_in_country(country):
  if country not in country_to_timezone:
    return "Sorry, I don't have information about that country."
  
  timezone_str = country_to_timezone[country]
  timezone = pytz.timezone(timezone_str)
  country_time = datetime.now(timezone)

  hour = country_time.hour

  if 5 <= hour <12:
    part_of_day = "morning"
  elif 12 <= hour < 17:
    part_of_day = "afternoon"
  elif 17 <= hour < 21:
    part_of_day = "evening"
  else:
    part_of_day = "night"

  time_str = country_time.strftime("%H:%M:%S")
  return f"It is currently {part_of_day} in {country}.The time is {time_str}."

def extract_date(input_str):
    # Regular expression pattern to match dates in the format dd month
    date_pattern = r'(\d{1,2})(?:st|nd|rd|th)?\s+(january|february|march|april|may|june|july|august|september|october|november|december)\b'
    
    # Match the date pattern in the input string
    match = re.search(date_pattern, input_str.lower())
    
    if match:
        # Extract day and month from the matched groups
        day = match.group(1)
        month_str = match.group(2)
        
        # Convert month string to a month number
        month = datetime.strptime(month_str, "%B").strftime("%m")
        
        # Format the date as dd-mm
        date_str = f"{day}-{month}"
        return date_str
    
    elif 'today' in input_str.lower():
        # If "today" is in the input string, return today's date in dd-mm format
        today_date = datetime.now().strftime("%d-%m")
        return today_date
    
    else:
        return None  # Return None if no valid date or "today" is found in the input
def get_recipe(query):
   api_key = "91c6aafd9c9c4e35acda94afae54e41f"
   url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={api_key}"
   response = requests.get(url)
   data = response.json()

   if 'results' in data and data['results']:
      recipe_id = data['results'][0]['id']
      details_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}"
      details_response = requests.get(details_url)
      recipe_details = details_response.json()
      return recipe_details
      
   else:
      return "no recipes found!"
   
def get_internet_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    res = st.results.dict()
    
    download_speed = res["download"] / 1_000_000  # Convert to Mbps
    upload_speed = res["upload"] / 1_000_000      # Convert to Mbps
    ping = res["ping"]
    
    result = f"Download speed: {download_speed:.2f} Mbps\nUpload speed: {upload_speed:.2f} Mbps\nPing: {ping} ms"
    return result
   
   
def number_guessing_game():
  correctNum = random.randint(1,100)
  userNum = -1
  guesses = 1
  # print(f"correctNum is: {correctNum}")

  while(userNum!=correctNum):
    
    speak("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        speak("Guess a number between 1 and 100.")
        user_guess = listen_game()
        if(user_guess == "exit"):
           speak("Jarvis: Shutting down. Goodbye!")
           sys.exit()
        print(user_guess)
        
        try:
            user_guess = int(user_guess)
            attempts += 1
            
            if user_guess < number_to_guess:
                speak("Too low! Try again.")
            elif user_guess > number_to_guess:
                speak("Too high! Try again.")
            else:
                speak(f"Congratulations! You've guessed the right number in {attempts} attempts.")
                break
        except ValueError:
            speak("Please say a valid number.")

def quiz_game():
  questions = {
        "movies": {
            "In which year was the movie 'Titanic' released?": "1997",
            "Who directed the movie 'Inception'?": "Christopher Nolan",
            "What is the name of the hobbit played by Elijah Wood in the Lord of the Rings movies?": "Frodo Baggins"
        },
        "sports": {
            "Which country won the Cricket World Cup in 2019?": "England",
            "Who is known as the 'God of Cricket'?": "Sachin Tendulkar",
            "How many players are there in a soccer team?": "11"
        },
        "games": {
            "Which game features characters named Mario and Luigi?": "Super Mario",
            "What is the highest-grossing video game of all time?": "Minecraft",
            "Which game involves collecting creatures called 'Pokémon'?": "Pokémon"
        },
        "general knowledge": {
            "What is the capital of India?": "New Delhi",
            "Who is the author of 'Harry Potter'?": "J.K. Rowling",
            "What is the largest mammal in the world?": "Blue Whale"
        }
    }

  score = 0
    
  speak("Welcome to the Quiz Game! Choose a category: movies, sports, games, or general knowledge.")
  category = listen_game().lower()
    
  if category not in questions:
    speak("Invalid category. Exiting the Quiz Game.")
    return
    
  speak(f"You chose {category}. Let's start the quiz!")
  for question, answer in questions[category].items():
    speak(question)
    user_answer = listen_game()
        
    if user_answer.lower() == answer.lower():
     speak("Correct!")
     score += 1
    else:
      speak(f"Wrong! The correct answer is {answer}.")
    
  speak(f"Your total score is {score} out of {len(questions[category])}.")


def send_whatsapp_msg(contact_name , message):

  # fetching contact number from dictionary
  contacts = phoneLibrary.contacts
  contact_number  = contacts.get(contact_name.lower())

  if not contact_number:
    speak(f"Contact {contact_name} not found.")
    return 
  
  contact_number = "+91" + contact_number

  # Schedule the message from a min from now

  hour = time.localtime().tm_hour
  minute = time.localtime().tm_min + 2

  kit.sendwhatmsg(contact_number,message,hour,minute)
  speak(f"Message sent to {contact_name}")

def search_youtube(query):
  try:
    kit.playonyt(query)
    return f"Searching for'{query} on Youtube..."
  except Exception as e:
    return f"Sorry, I encountered an error: {str(e)}"



  
tmdb_api_key = "4c2678e07c94923b96af3ba3fd8160a8"
base_url = "https://api.themoviedb.org/3"

def get_genre_id(genre_name):
    genres_url = f"{base_url}/genre/movie/list?api_key={tmdb_api_key}&language=en-US"
    response = requests.get(genres_url)
    genres = response.json()['genres']

    for genre in genres:
        if genre["name"].lower() == genre_name.lower():
            return genre["id"]
    return None  # Return None if genre_name is not found

def get_movie_recom(genre_name):
    genre_id = get_genre_id(genre_name)
    if not genre_id:
        return f"No genre found for {genre_name}."

    recommendations_url = f"{base_url}/discover/movie?api_key={tmdb_api_key}&with_genres={genre_id}&sort_by=popularity.desc"
    response = requests.get(recommendations_url)
    results = response.json()['results']

    recommended_movies = []
    for movie in results[:10]:  # Iterate over results, not results[10]
        recommended_movies.append(movie['title'])

    return recommended_movies

    
def google_search(query):
  try:
    kit.search(query)
    return f"Searching for'{query}' on Google..."
  except Exception as e:
    return f"Sorry, I encountered an error: {str(e)}"

# def aiProcess(command):
#   client = OpenAI(
#   # api_key="api_key",
#   )

#   completion= client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user", "content": command}
#     ]
# )

# Print the response
  # return completion.choices[0].message.content

def processCommand(c):
  print(c)

  

  if "open google" in c.lower():
    webbrowser.open("https://google.com")

  elif "open facebook" in c.lower():
    webbrowser.open("https://facebook.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://youtube.com")
  elif "open linkedin" in c.lower():
    webbrowser.open("https://linkedin.com")

  elif "open whatsapp" in c.lower():
    webbrowser.open("https://web.whatsapp.com/")

  elif "open twitter" in c.lower():
    webbrowser.open("https://x.com/home")

  elif "open chatgpt" in c.lower() or "open chat gpt" in c.lower():
    webbrowser.open("https://chatgpt.com/?oai-dm=1")

  elif "conversation" in c.lower():
     speak("Sure, I'd love to chat!")
     query = listen_game()

     if query in responses:
        speak(responses[query])
     else:
        speak("I dont have answer to that question currently")
     
  elif c.lower().startswith("play"):
    song = c.lower().split(" ")[1]
    link = musicLibrary.music[song]
    webbrowser.open(link)

  elif "news" in c.lower():
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=a60729d26fe942e394847c6a5d8d9c48")

    if r.status_code == 200:
      # Parse the JSON response
      data = r.json()

      # Extract the articles 
      articles = data.get('articles',[])

      if articles:
        # Print the headlines
        for article in articles[:5]:
          speak(article['title'])
      else:
        speak("No news articles found")

  elif "weather" in c.lower():
    city = c.split("weather in")[-1].strip()
    weather_report = get_weather(city)
    speak(weather_report)

  elif "recipe" in c.lower():
     dish = c.split("recipe of")[-1].strip()
     recipe = get_recipe(dish)
     if isinstance(recipe,dict):
        speak(f"Here is the recipe for {recipe['title']}.")
        print(f"Here is the recipe for {recipe['title']}.")
        speak("The ingredients are:")
        for ingredient in recipe['extendedIngredients']:
            speak(f" - {ingredient['original']}")
        
        speak("Now, the instructions:")
        speak(recipe['instructions'])
     else:
        speak(recipe)
        
  elif "play" in c.lower() and "games" in c.lower():
        speak("Welcome to Jarvis Games! Tell me which game you would like to play: Guess the Number or Quiz Game")
        choice = listen_game().lower()
        
        if "guess" in choice and "number" in choice:
            number_guessing_game()
        elif "quiz" in choice:
            quiz_game()
        elif "exit" in choice:
           sys.exit()
        else:
           speak("Invalid Game")
    

  elif "repeat this" in c.lower():
    speak("Okay, I am listening.")
    repeat_phrase()

  # elif "open focus mode" in c.lower():
  #   userInput = int(input("Are you sure you want to enter focus mode? [1 for YES / 2 for NO]: "))
  #   if userInput == 1:
  #       speak("Entering Focus Mode...")
  #       os.startfile(r"C:\Users\Japjot Singh\Desktop\Python\Projects\Jarvis\FocusMode.py")
  #       exit() 
  #   else:
  #       pass
    
  elif "check internet speed" in c.lower():
    speak("Checking internet speed. This may take a few seconds...")
    speed_result = get_internet_speed()
    speak(speed_result)
    print(speed_result)

  elif "date" in c.lower() and "today" in c.lower():
    today = datetime.today()

     # Extract day, month, and year
    day = today.day
    month = today.strftime("%B")  # Full month name
    year = today.year

    # Convert day to ordinal number format
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    # Format the date string
    date_string = f"Today is {day}{suffix} of {month}, {year}"

    speak(date_string)

  elif "time in" in c.lower():
    country = c.split("time in")[-1].strip()
    speak(get_time_in_country(country.lower()))

  elif "search on youtube" in c.lower():
    speak("What would you like to search on youtube?")
    try:
      with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for Youtube search query...")
        audio = recognizer.listen(source)
      query = recognizer.recognize_google(audio)
      print(f"Search query: {query}")
      speak(search_youtube(query))
    except Exception as e:
      speak(f"Sorry, I encountered an error: {str(e)}")

  elif "search on google" in c.lower():
    speak("What would you like to search on google?")
    try:
      with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for Google search query...")
        audio = recognizer.listen(source)
      query = recognizer.recognize_google(audio)
      print(f"Search query: {query}")
      speak(google_search(query))
    except Exception as e:
      speak(f"Sorry, I encountered an error: {str(e)}")

  elif "tell" in c.lower() and "joke" in c.lower():

    joke = pyjokes.get_joke()
    speak(joke)
    speak("Hope you enjoyed the joke! How may I assist you further?")

  elif "translate" in c.lower():

    speak("Which language would you like to translate to?")

    try:
        with sr.Microphone() as source:
          recognizer.adjust_for_ambient_noise(source)
          print("Listening for language to translate to...")
          audio = recognizer.listen(source)
        lang= recognizer.recognize_google(audio)
        print(f"dest language: {lang}")

        dest_lang_code = language_codes.get(lang.lower())

        speak("What would you like to translate")

        try:
          with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for translation query...")
            audio = recognizer.listen(source)
          query = recognizer.recognize_google(audio)
          print(f"Translation query: {query}")

          speak(get_translation(query,dest_lang_code))
          print(get_translation(query,dest_lang_code))
        except Exception as e:
          speak(f"Error:{str(e)}")

    except Exception as e:
      speak(f"Error: {str(e)}")

  elif "search on wikipedia" in c.lower():
    
      speak("What would you like to search on wikipedia?")
      try:
        with sr.Microphone() as source:
          recognizer.adjust_for_ambient_noise(source)
          print("Listening for wikipedia search query...")
          audio = recognizer.listen(source)
        query = recognizer.recognize_google(audio)
        print(f"Search query: {query}")

        page = wikipedia.page(query)

        url = page.url

        webbrowser.open(url)
        speak(f"Opening Wikipedia page for {query}.")
        
      except Exception as e:
        speak(f"Sorry, I encountered an error: {str(e)}")
      
  elif "celebrated on" in c.lower() or "occasion on" in c.lower():
    date_str = extract_date(c)

    if date_str:
        festive_info = festive_days.get(date_str)
        if festive_info:
            speak(festive_info)
        else:
            speak(f"No information found for {date_str}.")
    else:
        speak("Date extraction failed.")

  elif "message" in c.lower() and "whatsapp" in c.lower():
    speak("Type who would you like to message on whatsapp")

    # manually type your contact name and message 

    contact_name = input("Enter Contact name: ")
    speak(f"Type the message to send to {contact_name}")
    message = input("Enter message to send: ")
    send_whatsapp_msg(contact_name,message)

  elif "recommend" in c.lower() and "movies" in c.lower():
     genre = c.lower().split("recommend")[1].split("movie")[0].strip()

     recommendations = get_movie_recom(genre)

     if isinstance(recommendations, str):
        speak(recommendations)
        print(recommendations)
     else:
        speak(f"Top 10 {genre.capitalize()} Movies:")
        print(f"Top 10 {genre.capitalize()} Movies:")
        for idx, movie in enumerate(recommendations, 1):
          speak(f"{idx}. {movie}")
          print(f"{idx}. {movie}")


    # try:
    #   with sr.Microphone() as source:
    #     recognizer.adjust_for_ambient_noise(source)
    #     print("Listening for contact's name...")
    #     audio = recognizer.listen(source)
    #   contact_name = recognizer.recognize_google(audio)
    #   print(f"Recognized contact's name: {contact_name}")
    #   speak(f"What is the message for {contact_name}?")

    #   try:
    #       with sr.Microphone() as source:
    #         recognizer.adjust_for_ambient_noise(source)
    #         print("Listening for message...")
    #         audio = recognizer.listen(source)
    #       message = recognizer.recognize_google(audio)
    #       print(f"Message: {message}")
    #       send_whatsapp_msg(contact_name,message)
    #   except Exception as e:
    #       speak(f"Error:{str(e)}")
        
    # except Exception as e:
    #   speak("I didn't catch that. Please try again.")

  elif c.lower() in ["exit", "stop", "shutdown"]:
    speak("Jarvis: Shutting down. Goodbye!")
    sys.exit()

  else:
    # Let open ai handle request
      # output = aiProcess(c)
      # speak(output)
    
    # wikipedia function to get info 
    try:
      summary = wikipedia.summary(c,sentences=3)
      speak(summary)
    except Exception as e:
      speak(f"An error occurred: {e}")

if __name__ == "__main__":
  speak("Initializing Jarvis....")
  introduction = (
        "Hello, I am Jarvis, your personal voice assistant. "
        # "I am here to help you with various tasks, provide information, and make your life easier. "
        "How can I assist you today?"

    )
  

  speak(introduction)
  while True:
    r = sr.Recognizer()
    # Listen for the wake word "Jarvis"
    # obtain audio from the microphone
  
    # recognize speech using google
    try:
       
      with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source , timeout=5)
      word = r.recognize_google(audio)
      if(word.lower() == "jarvis"):
        speak("Yes, how can I assist you?")
        # Listen for command
        with sr.Microphone() as source:
          recognizer.adjust_for_ambient_noise(source)
          
          print("Jarvis Activated...")
          audio = r.listen(source)
          command = r.recognize_google(audio)

          processCommand(command)

    except Exception as e:
      print("Error; {0}".format(e))

