# Create title
# Create Start Button 
    #PopUp/alert/modal
    #Text Window: Your Name
    #Enter Button
# Install Flet (pip install flet)

# Create system function

import flet as ft

def main(page):
    #Create
    title = ft.Text("ZAP")
    chat = ft.Column()
    username = ft.TextField(label="Enter your name")

    page.bgcolor = "#0E0054"

    def send_tunelmessage(message):
        tipe = message["tipe"]
        if tipe == "message":
            text_message = message["text"]
            user_message = message["user"]
            #ADD Message
            chat.controls.append(ft.Text(f"{user_message}: {text_message}"))
        else:
            user_message = message["user"]
            chat.controls.append(ft.Text(f"{user_message} enter chat", 
                                         size=12, italic=True, color=ft.colors.ORANGE_500))
        page.update()

    page.pubsub.subscribe(send_tunelmessage)

    def sendmessage(event):
        page.pubsub.send_all({"text": message.value, "user": username.value,                 
                              "tipe": "message"})
        # Clean Message
        message.value = ""
        page.update()
    message = ft.TextField(label="Type message", on_submit=sendmessage)  
    send_button = ft.ElevatedButton("SEND", on_click=sendmessage)  

    def enter_popup(event):
        page.pubsub.send_all({"user": username.value, "tipe": "enter"})
        page.add(chat)
        popup.open = False

        page.remove(title)
        page.remove(start_button)
        
        #add
        page.add(ft.Row(
            [message, send_button]
        ))
        page.update()

    

    popup = ft.AlertDialog( 
        open=False, 
        modal=True,
        title=ft.Text("Welcome to ZAP"),
        content=username,
        actions=[ft.ElevatedButton("Enter", on_click=enter_popup)],
        )


    def enter_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()   

    start_button = ft.ElevatedButton("Start Chat", on_click=enter_chat)
    
    #Add
    page.add(title)
    page.add(start_button)
    

# System Execute
ft.app(target=main)

