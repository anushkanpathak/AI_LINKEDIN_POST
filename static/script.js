// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("uploadForm");
//   const fileInput = document.getElementById("transcriptFile");
//   const resultDiv = document.getElementById("result");

//   form.addEventListener("submit", async function (e) {
//     e.preventDefault();
//     resultDiv.innerHTML = "Generating post... ⏳";

//     const file = fileInput.files[0];
//     if (!file) {
//       resultDiv.innerHTML = "Please upload a transcript file.";
//       return;
//     }

//     const formData = new FormData();
//     formData.append("transcript", file);

//     try {
//       const response = await fetch("/", {
//         method: "POST",
//         body: formData,
//       });

//       const text = await response.text();
//       resultDiv.innerHTML = text;
//     } catch (error) {
//       console.error("Error:", error);
//       resultDiv.innerHTML = "Something went wrong.";
//     }
//   });
// });

// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("uploadForm");
//   const fileInput = document.getElementById("transcriptFile");
//   const resultDiv = document.getElementById("result");

//   form.addEventListener("submit", async function (e) {
//     e.preventDefault();
//     resultDiv.innerHTML = "Generating post... ⏳";

//     const file = fileInput.files[0];
//     if (!file) {
//       resultDiv.innerHTML = "Please upload a transcript file.";
//       return;
//     }

//     const formData = new FormData();
//     formData.append("transcript", file);

//     try {
//       const response = await fetch("/generate", {
//         method: "POST",
//         body: formData,
//       });

//       const data = await response.json();
//       if (data.post) {
//         resultDiv.innerHTML = `<h3>Generated LinkedIn Post:</h3><p>${data.post}</p>`;
//       } else {
//         resultDiv.innerHTML = "❌ Failed to generate post.";
//       }
//     } catch (error) {
//       console.error("Error:", error);
      
//       resultDiv.innerHTML = "❌ Something went wrong while generating the post.";
//     }
//   });
// });

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("uploadForm");
  const fileInput = document.getElementById("transcriptFile");
  const resultDiv = document.getElementById("result");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    resultDiv.innerHTML = "Generating post... ⏳";

    const file = fileInput.files[0];
    if (!file) {
      resultDiv.innerHTML = "❌ Please upload a transcript file.";
      return;
    }

    const formData = new FormData();
    formData.append("transcript", file);

    try {
      const response = await fetch("/generate", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      if (data.post) {
        resultDiv.innerHTML = `<h3>Generated LinkedIn Post:</h3><pre>${data.post}</pre>`;
      } else {
        resultDiv.innerHTML = "❌ Failed to generate post.";
      }
    } catch (error) {
      console.error("Error:", error);
      resultDiv.innerHTML = "❌ Something went wrong while generating the post.";
    }
  });
});
