"use client"
import React, { useState } from 'react';
import { useSpeechSynthesis } from 'react-speech-kit';

export default function Example() {
    const [value, setValue] = useState('');
    const { speak, voices } = useSpeechSynthesis();
    const selectedVoice = voices.find(voice => voice.lang.includes('ar-SA'));

    speechSynthesis.onvoiceschanged = function () {
        var voices = this.getVoices();
        console.log(voices);
      };

    return (
        <div>
            <textarea
                value={value}
                onChange={(event) => setValue(event.target.value)}
            />
            <button onClick={() => speak({ text: value, voice: selectedVoice })}>Speak</button>
        </div>
    );
}