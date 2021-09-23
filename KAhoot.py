"""
 __    __           __                             __     
|  \  /  \         |  \                           |  \    
| $$ /  $$ ______  | $$____    ______    ______  _| $$_   
| $$/  $$ |      \ | $$    \  /      \  /      \|   $$ \  
| $$  $$   \$$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\\$$$$$$  
| $$$$$\  /      $$| $$  | $$| $$  | $$| $$  | $$ | $$ __ 
| $$ \$$\|  $$$$$$$| $$  | $$| $$__/ $$| $$__/ $$ | $$|  \
| $$  \$$\\$$    $$| $$  | $$ \$$    $$ \$$    $$  \$$  $$
 \$$   \$$ \$$$$$$$ \$$   \$$  \$$$$$$   \$$$$$$    \$$$$ 
                                                          
                                                          
https://github.com/vmthread/ 
https://kahootbotter.com <- Just got tapped :)
"""




import requests,os,sys,time,threading,json





class Kahoot():
    def __init__(self):
        self.discord = "https://discord.gg/dw5m8deCv4"
        self.url = 'https://kahootbotter.com/api/graphql'
        self.headers = {
        'authority': 'kahootbotter.com',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'accept': '*/*',
        'content-type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://kahootbotter.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://kahootbotter.com/',
        'accept-language': 'en-US,en;q=0.9'
        }




    def joinkahoot(self,code,username):
        payload = json.dumps({
        "operationName": "spawnBots",
        "variables": {
            "botName": f"{username}",
            "gamePin": f"{code}",
            "botAmount": 50
        },
        "query": "mutation spawnBots($botName: Stringu0021, $gamePin: Intu0021, $botAmount: Intu0021) {\n  spawnBots(botName: $botName, gamePin: $gamePin, botAmount: $botAmount) {\n    title\n    status\n    description\n    __typename\n  }\n}\n"
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        print(response.text)
    
class EnterSession():
    def __init__(self):
        os.system("cls && title Github.com/vmthread")
        print(f'''
        


  ________                                              __ 
|        \                                            |  \
 \$$$$$$$$______    ______    ______    ______    ____| $$
   | $$  |      \  /      \  /      \  /      \  /      $$
   | $$   \$$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$$
   | $$  /      $$| $$  | $$| $$  | $$| $$    $$| $$  | $$
   | $$ |  $$$$$$$| $$__/ $$| $$__/ $$| $$$$$$$$| $$__| $$
   | $$  \$$    $$| $$    $$| $$    $$ \$$     \ \$$    $$
    \$$   \$$$$$$$| $$$$$$$ | $$$$$$$   \$$$$$$$  \$$$$$$$
                  | $$      | $$                          
                  | $$      | $$                          
                   \$$       \$$                                                                                   
                                                          
                                                          
        
        
        ''')
if __name__ == '__main__':
    EnterSession()
    usn = input("Username: ")
    gamp = input("Gamepin: ")
    Kahoot().joinkahoot(gamp,usn)
