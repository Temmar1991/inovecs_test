from socketIO_client import SocketIO, LoggingNamespace
import os
sock = SocketIO(f'http://{os.environ.get("HOST")}', 9000)


def backup_event(message):
    print(f"Backup file {message['file_name']}, size {message['file_size']} is done at time {message['date']}")


def failed_backup(mes):
    print(f"Backup failed. Please check logs.")


sock.on('backup_successful', backup_event)
sock.on('backup_failed', failed_backup)


if __name__ == '__main__':
    sock.wait()
