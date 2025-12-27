</head>
<body>
  <h1>Pickle (.pkcls) File Inspector</h1>

  <p>
    This project provides a Python script to <strong>scan the current directory for .pkcls files</strong>,
    load them, extract key object details, and save a comprehensive summary into a single text file.
    It is designed as a <strong>utility repository for app deployment</strong> and for community benefit.
  </p>

  <h2>Features</h2>
  <ul>
    <li><strong>Automatic Detection:</strong> Finds all .pkcls files in the current directory.</li>
    <li><strong>Object Inspection:</strong> Loads each file and retrieves attributes like name, parameters, 
        original data, and underlying scikit-learn model info (if applicable).</li>
    <li><strong>Hyperparameters & Metadata:</strong> Extracts model hyperparameters, feature importances, 
        and other relevant properties.</li>
    <li><strong>Consolidated Output:</strong> Saves a detailed report of all .pkcls files into one text file.</li>
    <li><strong>Safe Handling:</strong> Warnings and errors are managed to avoid crashes during batch inspection.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>Clone or download the repository.</li>
    <li>Install required Python libraries:
      <pre><code>pip install numpy joblib Orange3</code></pre>
    </li>
    <li>Run the Python script:
      <pre><code>python PKCLS_Inspector.py</code></pre>
    </li>
    <li>The script will:
      <ul>
        <li>Scan the current folder for all .pkcls files.</li>
        <li>Load and inspect each object.</li>
        <li>Save the extracted information into a single text file named <code>pkcls_Summary.txt</code>.</li>
      </ul>
    </li>
  </ol>

  <h2>Requirements</h2>
  <ul>
    <li>Python 3.12</li>
    <li>Libraries: numpy, joblib, Orange3</li>
    <li>.pkcls files located in the same directory as the script</li>
  </ul>

  <h2>License</h2>
  <p>
    This project is licensed under the <strong>MIT License</strong>. You may use, modify, and redistribute 
    the code, but <strong>credit to the original developer is required</strong>. Commercial use requires explicit permission.
  </p>

  <h2>Developer Info</h2>
  <ul>
    <li><strong>Developer:</strong> Engr. Tufail Mabood</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874">WhatsApp</a></li>
    <li><strong>Note:</strong> This repository is for inspecting .pkcls files and saving summaries. Contributions and improvements are welcome.</li>
  </ul>
</body>
