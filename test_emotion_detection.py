from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        # Test statment for 'joy'
        resp1  = emotion_detector("I am glad this happened")
        self.assertEqual(resp1['dominant_emotion'],'joy')

        # Test statment for 'anger'
        resp1  = emotion_detector("I am really mad about this")
        self.assertEqual(resp1['dominant_emotion'],'anger')

        # Test statment for 'disgust'
        resp1  = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(resp1['dominant_emotion'],'disgust')

        # Test statment for 'sadness'
        resp1  = emotion_detector("I am so sad about this")
        self.assertEqual(resp1['dominant_emotion'],'sadness')

        # Test statment for 'fear'
        resp1  = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(resp1['dominant_emotion'],'fear')

if __name__ == '__main__':
    unittest.main()
    