class Node:
    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    # Add a song to the end
    def add(self, title):
        new_node = Node(title)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Print the full playlist
    def show(self):
        current = self.head
        songs = []
        while current:
            songs.append(current.title)
            current = current.next
        print(" -> ".join(songs))

    # Remove a song by name
    def delete(self, title):
        if not self.head:
            return
        
        # If the song to delete is the first song
        if self.head.title == title:
            self.head = self.head.next
            return

        # Look for the song in the rest of the list
        current = self.head
        while current.next:
            if current.next.title == title:
                current.next = current.next.next  # Skip over the deleted node
                return
            current = current.next


playlist = Playlist()

# Create initial playlist and add Song4
playlist.add("Song1")
playlist.add("Song2")
playlist.add("Song3")
playlist.add("Song4")

print("Playlist after adding Song4:")
playlist.show()

# Delete Song2
playlist.delete("Song2")

print("\nPlaylist after deleting Song2:")
playlist.show()