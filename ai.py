#%%
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
 
 Ask the bot any questions to train its understanding of diffrent words.
 Type "bye" to quit 
 """)

try:
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
 
    cursor.execute('SELECT key from data')
    keywords = [row[0] for row in cursor.fetchall()]

    cursor.execute('SELECT res from data')
    responses = [row[0] for row in cursor.fetchall()]

    # print(keywords)
    # print(responses)

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
        new_response = input("bot: I haven't heard that word before, how should I respond to " + word + "? ")
        responses.append(new_response)
        keywords.append(word)
        print("bot: ait, " + new_response)

    word = input("You: ").lower()
    

try:
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    conn.execute('CREATE TABLE IF NOT EXISTS data (key TEXT, res TEXT)')

    teller = 0
    while (teller < len(keywords)):
        
        conn.execute('INSERT INTO data (key,res) VALUES (?,?)',(keywords[teller],responses[teller]))  
        teller = teller + 1   
    
    conn.commit()
    conn.close()

    print(random.choice(goodbyes))

except sqlite3.Error as error:
    print("Error while working with SQLite :", error)
finally:
    if conn:
        conn.close
    

# %%
