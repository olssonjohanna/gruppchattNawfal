from server.ChattViewer import ChattViewer
from server.Listener import Listener

listener = Listener()
listener.acceptConnection()

chattV = ChattViewer(listener)
chattV.buildGui()

listener.startReceiver(chattV)
chattV.start()