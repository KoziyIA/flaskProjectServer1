from flask import Flask, request

app = Flask(__name__)
ListOfMessages = []

@app.route('/')
def hello_world():
    return 'Messenger Flask server is running'  \
            '<br> <a href="/status">Check status</a>'

@app.route('/status')
def status():
    return {
        'messages_count': len(ListOfMessages)
    }

@app.route("/api/Messenger", methods=['POST'])
def SendMessage():
    msg = request.json
    print(msg)
    ListOfMessages.append(msg)
    msgtext = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Messages overall: {len(ListOfMessages)}, message sent: {msgtext}")
    return f"Message sent success. Messages overall: {len(ListOfMessages)}", 200

@app.route("/api/Messenger/<int:id>")
def GetMessage(id):
    print(id)
    if id >= 0 and id < len(ListOfMessages):
        print(ListOfMessages[id])
        return ListOfMessages[id], 200
    else:
        return "Not found 1", 400

if __name__ == '__main__':
    app.run()
#    app.run(host = 'localhost', port = 5001)
