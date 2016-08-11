# social-network-graph
Provides a relational graph (nodes and edges) representing the relationships between facebook friends

## Instructions:
 * Log into your Facebook account
 * Navigate to your friends page
 * Scroll to the very bottom
 * Open Chrome developer tools
 * Click on the `Console` tab
 * Click the sub-tab labeled `Logs`
 * Paste the contents of `harvest.js` into the console and press enter
 * Right click on the output, click `Save as...`
 * Save the file as the person's name (verbatim) `.log` from who's friend list you downloaded (ex. `Thomas Gerot.log`)

 Repeat process for individuals you want to add to your data
 
 * Move all the `.log` files to a single folder
 * Move that folder into the same directory as visualize.py
 * Make a directory in that same directory called `graphs`
 * Run visualize.py and respond to the inputs
