import sqlite3

conn = sqlite3.connect('video.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               length TEXT NOT NULL
)
''')

def list_videos():
    data = cursor.execute("SELECT * FROM videos")
    for row in data.fetchall():
        print(row)


def add_video(new_name,new_length):
    cursor.execute("INSERT INTO videos (name, length) VALUES (?,?)",(new_name, new_length))
    conn.commit()
    print("### Video Added ###")

def update_video(vid_id, new_name, new_length):
    cursor.execute("UPDATE videos SET name=(?), length=(?) WHERE id =(?)", (new_name, new_length, vid_id))
    conn.commit()
    print("### Video Updated ###")

def delete_video(vid_id):
    cursor.execute("DELETE FROM videos WHERE id = (?)", (vid_id,))
    conn.commit()
    print("### Video Deleted ###")

def main():
    while True:
        print("Welcome to YouTube Manager")
        print('''
                1. List all Videos
                2. Add new Video
                3. Update Video
                4. Delete Video
                5. Close 
        ''')
        choice = input("Please select any choice to perform! ")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Name of video: ")
            length = input("Duration of video: ")
            add_video(name,length)
        elif choice == '3':
            vid_id = input("Select video ID to update: ")
            name = input("Updated Name of video: ")
            length = input("Updated Duration of video: ")
            update_video(vid_id, name, length)
        elif choice == '4':
            vid_id = input('Name video ID to delete ')
            delete_video(vid_id)
        elif choice == '5':
            break
        else:
            print("Please Enter Valid Choice:")

    conn.close()

if __name__ == "__main__":
    main()

print("Thankyou !!")