import random
import sqlite3

print("""



                                                                              ________________________________________
                                                                             |                                        | 
                                                                             |                                        | 
                                                                             |                                        | 
                                                                             |               Chatbot69                |
                                                                             |                by ludd3                | 
                                                                             |                                        | 
                                                                             |                                        | 
                                                                             |________________________________________|
 
 Ask the bot any questions to train its understanding of different words.
 Type "bye" to quit 
 """)

try:
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT key, res from data')
    data = cursor.fetchall()

    keywords = [row[0] for row in data]
    responses = [row[1] for row in data]

except sqlite3.Error as error:
    print("Error while working with SQLite :", error)


finally:
    if conn:
        cursor.close()


greetings = ["bot: Hey!", "bot: Hello!", "bot: Hi!"]
goodbyes = ["Bye!", "Goodbye!", "Cya l8r"]


print(random.choice(greetings))

word = input("You: ").lower()


while word != "bye":
    keyword_found = False

    for index, keyword in enumerate(keywords):
        if keyword in word:
            print("bot: " + responses[index])
            keyword_found = True
            break

    if not keyword_found:
        new_response = input(
            "bot: I haven't heard that word before, how should I respond to " + word + "? ")
        responses.append(new_response)
        keywords.append(word)
        print("bot: ait, " + new_response)

    word = input("You: ").lower()


try:
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM data')

    for i in range(len(keywords)):
        cursor.execute('INSERT INTO data (key,res) VALUES (?,?)',
                       (keywords[i], responses[i]))

    conn.commit()

    print(random.choice(goodbyes))

except sqlite3.Error as error:
    print("Error while working with SQLite :", error)
finally:
    if conn:
        conn.close()
