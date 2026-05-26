// ===== 播放控制逻辑 =====
        const audio = document.getElementById('bgm');
        const playBtn = document.getElementById('playBtn');
        
        if (!audio) {
            console.error('音频元素未找到: id="bgm"');
        }
        if (!playBtn) {
            console.error('播放按钮未找到: id="playBtn"');
        }
        
        function togglePlay() {
            if (!audio) return;
            if (audio.paused) {
                audio.play().catch(error => {
                    console.error('播放失败：', error);
                });
                playBtn?.classList.add('playing');
            } else {
                audio.pause();
                playBtn?.classList.remove('playing');
            }
        }
        
        audio?.addEventListener('ended', function() {
            playBtn?.classList.remove('playing');
        });
        
        audio?.addEventListener('error', function(event) {
            console.error('音频加载/播放错误', event, audio?.currentSrc, audio?.error);
        });