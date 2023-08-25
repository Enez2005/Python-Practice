# challenges

#FIZZBUZZ

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else: print(index)
fizzbuzz()

#Es un Anagrama?

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

    

print(is_anagram("Imagine Dragons", "Ragged Insomnia"))

#Fibonnacci

def fibonacci():

    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)

        fib = prev + next
        prev = next
        next = fib


fibonacci()

#Es Primo?

def is_prime (x):

    divisores = 0
    for i in range(1, x + 1):
        if x % i == 0:
            divisores += 1
        if divisores > 2:
            break
    if divisores == 2:
            return True
    else:
        return False

print(is_prime(829))

#Invertir palabra

def invertir(text):
    reversed_text = ""
    for elements in range(0, len(text)):
        reversed_text += text[-(elements+1)]
    return reversed_text


print(invertir("Amigo Mio"))