import React from 'react';

const ArabicNumberSpeaker = () => {
  const speakNumber = (number) => {
    if (number < 1 || number > 999) {
      console.error('Number must be between 1 and 999');
      return;
    }

    const utterance = new SpeechSynthesisUtterance(number.toString());

    // Find an Arabic voice
    const voices = window.speechSynthesis.getVoices();
    const arabicVoice = voices.find(voice => voice.lang.startsWith('ar-EG'));

    if (arabicVoice) {
      utterance.voice = arabicVoice;
    } else {
      console.warn('Arabic voice not found');
    }

    window.speechSynthesis.speak(utterance);
  };

  return (
    <div>
      <input
        type="number"
        min="1"
        max="999"
        onChange={(e) => speakNumber(e.target.value)}
        placeholder="Enter a number"
      />
    </div>
  );
};

export default ArabicNumberSpeaker;
