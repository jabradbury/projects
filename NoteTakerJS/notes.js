const noteTextArea = document.getElementById('input-box');
const addNoteBtn = document.getElementById('add-note');
const noteStorageList = document.getElementById('note-storage-list');
const titleBox = document.getElementById('title-box');
const expandButtons = document.getElementsByClassName('expand-btn');
const modal = document.getElementById('modal');
const modalTitle = document.getElementById('modal-title');
const modalContent = document.getElementById('modal-content');
const modalClose = document.querySelector('.modal .close');
const maxNoteLength = 50;

// Retrieve notes from localStorage on page load
window.addEventListener('load', function() {
  const storedNotes = JSON.parse(localStorage.getItem('notes'));
  if (storedNotes) {
    storedNotes.forEach(function(note) {
      addNoteToList(note.title, note.text);
    });
  }
});

// Add note to the list and store in localStorage
function addNoteToList(title, text) {
  const listItem = document.createElement('li');
  const noteDiv = document.createElement('div');
  noteDiv.className = 'note';
  const noteHeading = document.createElement('h4');
  noteHeading.innerHTML = title;
  const noteParagraph = document.createElement('p');
  const truncatedNoteText = text.length > maxNoteLength ? text.substring(0, maxNoteLength) + '...' : text;
  noteParagraph.innerHTML = truncatedNoteText;
  noteParagraph.dataset.fullText = text; // Store the full text as a data attribute

  const expandButton = document.createElement('button');
  expandButton.className = 'expand-btn';
  expandButton.textContent = 'View Detail';

  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'Delete';
  deleteButton.addEventListener('click', function() {
    listItem.remove();
    removeNoteFromStorage(title, text);
  });

  noteDiv.appendChild(noteHeading);
  noteDiv.appendChild(noteParagraph);
  noteDiv.appendChild(expandButton);
  noteDiv.appendChild(deleteButton);
  listItem.appendChild(noteDiv);
  noteStorageList.appendChild(listItem);
}

// Event listener for adding a new note
addNoteBtn.addEventListener('click', function() {
  const noteText = noteTextArea.value;
  const noteTitle = titleBox.value;
  if (noteText.trim() !== '' && noteTitle.trim() !== '') {
    addNoteToList(noteTitle, noteText);

    // Store note in localStorage
    const storedNotes = JSON.parse(localStorage.getItem('notes')) || [];
    storedNotes.push({ title: noteTitle, text: noteText });
    localStorage.setItem('notes', JSON.stringify(storedNotes));

    noteTextArea.value = '';
    titleBox.value = '';
  }
});

// Function to remove note from localStorage
function removeNoteFromStorage(title, text) {
  const storedNotes = JSON.parse(localStorage.getItem('notes')) || [];
  const updatedNotes = storedNotes.filter(function(note) {
    return !(note.title === title && note.text === text);
  });
  localStorage.setItem('notes', JSON.stringify(updatedNotes));
}

// Function to open the modal
function openModal(title, content) {
  modalTitle.textContent = title;
  modalContent.textContent = content;
  modal.style.display = 'block';
}

// Function to close the modal
function closeModal() {
  modal.style.display = 'none';
}

// Attach event listener to noteStorageList using event delegation
noteStorageList.addEventListener('click', function(event) {
  if (event.target.classList.contains('expand-btn')) {
    const noteDiv = event.target.parentNode;
    const noteTitle = noteDiv.querySelector('h4').innerHTML;
    const noteParagraph = noteDiv.querySelector('p');
    const noteText = noteParagraph.dataset.fullText;
    openModal(noteTitle, noteText);
  }
});

// Close modal when the close button is clicked
modalClose.addEventListener('click', closeModal);

// Close modal when the user clicks outside the modal
window.addEventListener('click', function(event) {
  if (event.target === modal) {
    closeModal();
  }
});
