from math import sqrt
import speech_recognition as sr
r = sr.Recognizer()




while True:
    try:
        with sr.Microphone(device_index=1) as source:
            print("я готов к работе")
            audio = r.listen(source)
            speech = r.recognize_google(audio, language='ru_RU').lower()
            if speech == "помоги решить квадратное уравнение":
                print("c радостью. Сообщи мне коэфициенты  квадртаном уравнении поочерёдно")
                count = 0
                numbers = []
                while count < 3:
                    audio = r.listen(source)
                    speech = r.recognize_google(audio, language='ru_RU').lower()
                    if speech == "минус один":
                        speech = "-1"
                    if " " in speech:
                        speech_1 = speech.replace(" ", "")
                        numbers.append(speech_1)                                                          
                    else:
                        numbers.append(speech)                  
                    count += 1                              
                    print(f'Коэфициент {count} сообщён')               
                print(numbers)
                a = int(numbers[0])                   
                b = int(numbers[1])             
                c = int(numbers[2])
                D = b**2 - 4*a*c
                if D < 0:                                 
                    print("Уравнение не имеет корней")
                else:

                    x1 = (-b+sqrt(D))/(2*a)
                    x2 = (-b-sqrt(D))/(2*a)
                    # def change_1_to_noth(x):
                    #     if x == '1':
                    #         x=""
                    # change = map(change_1_to_noth, numbers)
                    print(f'Уравнение принимает следующий вид: {numbers[0]}x**2 + {numbers[1]}x + {numbers[2]} = 0 \nУравнение имеет следующие корни: {x1}, {x2}')

                

        
    except sr.UnknownValueError:
        print("Голос не был распознан")
