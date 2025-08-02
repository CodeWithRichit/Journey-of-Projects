import random
import time 

test_sente=['The stars sparkled brightly in the midnight sky.',
'Never trust a mirror, it always shows less.',
'Rain tapped gently on the old wooden window frame.',
'He walked away without saying a single word.',
'The desert wind whispered secrets no one understood.',
'Every decision you make builds your entire future.',
'Music filled the hall with soft, golden light.',
'The cat leaped silently onto the dusty bookshelf.',
"Books are windows to worlds you haven't seen.",
'Time slows down when memories come rushing back.',
'Shadows danced across the wall as candles flickered.',
'The clock ticked loudly in the silent room.',
'No plan survives the first punch in life.',
'Dreams drifted through his mind like passing clouds.',
'Her laughter echoed across the empty summer field.',
'He searched for meaning in an unread letter.',
'The forest whispered stories older than mankind itself.',
'The lighthouse stood tall against crashing ocean waves.',
'He stared into space, lost in deep thought.',
'Mist rolled across the valley like a veil.',
'Silence often speaks louder than any spoken word.',
'The mountain path twisted higher into the clouds.',
'They waited quietly beneath the shadow of giants.',
'The sun rose slowly behind distant snowy peaks.',
'Hope is found in the smallest warm gesture.',
'He smiled nervously before stepping onto the stage.',
'The dog barked twice, then ran into trees.',
'She found courage in the darkest of moments.',
'Every sunset brings a promise of new beginnings.',
'A single leaf floated gently to the ground.',
'They walked slowly, hand in hand, under moonlight.',
'Fear grows stronger when left unspoken for long.',
"The candle's flame flickered like a frightened heart.",
'Her voice trembled like wind rustling dry leaves.',
'The key was hidden beneath the old floorboard.',
'He left behind memories no one could erase.',
'The stars aligned for only a fleeting second.',
'In silence, she discovered what truly mattered most.',
'A letter arrived with no name or address.',
'The storm passed, leaving puddles in broken streets.',
'She painted dreams on walls no one saw.',
'Even silence can be loud in lonely times.',
'The fire crackled while stories warmed cold hearts.',
'The river carried secrets deep beneath its surface.',
'He chased the train but never caught it.',
'Time heals some wounds, but scars always remain.',
'Her eyes told stories she never dared speak.',
'Old photographs are frozen whispers from the past.',
'He waited hours just to see her smile.',
'She danced under stars with tears in eyes.',
'The wind howled louder than her broken cries.',
]
while True:
    Ask=input('Hey!Do you want to check your typing speed,(Yes/No): ').lower() #Asking the user whether he wants to play or not.
    if Ask=='yes': #If he agrees
     n=int(input('How many sentences you want, to check your typing speed.Choose from [1,50]: '))#Ask number of sentences he wants to type.
     if n<1:
        print('Please enter number of sentences,above 0')
     elif n>50:
        print('Please enter number of sentences,below 50')
     else:
        selected_sentences=random.sample(test_sente,n)#random.sample,helps to choose random sentence each time you play.n=no.of sentences,test_sente=polpulation from wherethese comes
        print(selected_sentences)
        total_time=0
        count=0
        for i in selected_sentences:# this loops over the n sentences and present them one by one.
         print(i)
         start_time=time.time()#as soon as the sentences get displayed,timer starts.
         user_inp=input('Type the sentence: ')
         end_time=time.time()#when one sentence is typed,the clock is stopped
         time_taken=round(end_time-start_time,2) #it gives decimals digit and rounded upto 2,#calcuates time taken to write a sentence.
         total_time=time_taken+total_time# time taken to write every sentence
         print(f"⏱ Time taken: {time_taken} seconds")
         if user_inp==i:
          print('Correct')
          count=count+1  #counts the number of correct sentences
         else:
          print('Incorrect')

        avg_time = round(total_time / n, 2)
        print(f"🕐 Average time per sentence: {avg_time} seconds")
        print('You got',count,'on',n)
        if count==n:
          print('Good Job!🔥') 
        elif count<n:
          print('Practice makes perfect!👍')
    elif Ask=='no':
      print('Thanks!but please do check this out next,time.')
      break
      
    
     