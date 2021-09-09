from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Song

# Create your tests here.
class MusicTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', email='test@email.com', password='pass')
        testuser1.save()

        test_song = Song.objects.create(
            title='Gravity',
            artist='Sara Bareilles',
            genre='Pop',
            listener=testuser1
        )
        test_song.save()
    
    def test_song_item(self):
        song = Song.objects.get(id=1)
        actual_title=str(song.title)
        actual_artist=str(song.artist)
        actual_genre=str(song.genre)
        actual_listener=str(song.listener)
        self.assertEqual(actual_title, 'Gravity')
        self.assertEqual(actual_artist, 'Sara Bareilles')
        self.assertEqual(actual_genre, 'Pop')
        self.assertEqual(actual_listener, 'testuser1')