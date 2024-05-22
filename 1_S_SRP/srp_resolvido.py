from TaskHandler import TaskHandler
from APIHandler import APIHandler
from NotificatorHandler import NotificatorHandler
from ReportHandler import ReportHandler

apiHandler = APIHandler()
taskHandler = TaskHandler()
notificatorHandler = NotificatorHandler()
reportHandler = ReportHandler()

apiHandler.conect_api()
taskHandler.create_task()
notificatorHandler.send_notification()
taskHandler.update_task()
notificatorHandler.send_notification()
taskHandler.remove_task()
notificatorHandler.send_notification()
reportHandler.generate_report()
reportHandler.send_report()
