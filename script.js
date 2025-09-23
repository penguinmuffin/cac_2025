// Practice page mode button logic
document.addEventListener('DOMContentLoaded', function() {
	const presentationBtn = document.getElementById('presentationBtn');
	const interviewBtn = document.getElementById('interviewBtn');
	if (presentationBtn && interviewBtn) {
		presentationBtn.onclick = () => {
			presentationBtn.classList.add('active');
			interviewBtn.classList.remove('active');
		};
		interviewBtn.onclick = () => {
			interviewBtn.classList.add('active');
			presentationBtn.classList.remove('active');
		};
	}
	// Future: handle start button logic here
});


// Simple dropdown hover logic
document.querySelectorAll('.dropdown').forEach(function(drop) {
	drop.addEventListener('mouseenter', function() {
		var content = drop.querySelector('.dropdown-content');
		if(content) content.style.display = 'block';
	});
	drop.addEventListener('mouseleave', function() {
		var content = drop.querySelector('.dropdown-content');
		if(content) content.style.display = 'none';
	});
});