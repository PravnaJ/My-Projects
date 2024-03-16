# freecodecamp-practice
<!DOCTYPE html>
 <html lang="em">
   <head>
    <link rel="stylesheet" href="styles.css" />
   </head>
   <body>
     <div class="container">
       <header id="header">
         <h1 id="title" class="text=center">JP's form<h1>
           <p id="description" class="description text-center">Thank you for taking yoour time for filling this form</p>
           </header>
     <form id="survey-form">
       <div class="form group">
         <label id="name-label" for="name">Name</label>
         <input type="text" name="name" id="name" class="form-control" placeholder="Enter Your Name" required>
       </div>

       <div class="form group">
          <label id="email-label" for="email">email</label>
         <input type="email" name="email" id="email" class="form-control" placeholder="Enter Your Email" required>
       </div>

       <div class="form group">
         <label id="number-label" for="number">
           "Age"
           <span class="clue">(optional)</span>
           </label>
           <input type="number" name="age" id="number" min="10" max="99" class="form-control" placeholder="Age">
       </div>

       <div class="form group">
         <p>which option best describes your current role?</p>
         <select id="dropdown" name="role" class="form-control" required>
           <option disabled selected value>Select currnt role</option>
           <option value="student">Student</option>
           <option value="student">Full Time Job</option>
           <option value="student">Full Time Learner</option>
           <option value="student">Prefer Not to Say</option>
         </select> 
       </div>
       
       <div class="form group">
         <p>Would you recommend JP OAHAponics to a friend</p>
         <label>
           <input name="user-recommend" value="definitely" type="radio" class="input-radio" checked>
           "Definitely"
           </label>
           <label>
             <input name="user-recommend" value="not-sure" type="radio" class="input-radio">
             "Maybe"
             </label>
             <label>
             <input name="user-recommend" value="not-sure" type="radio" class="input-radio">
             "Not Sure"
             </label>
       </div>

       <div class="form group">
         <p>What is your favorite feature of JP OAHAponics?</p>
         <select id="most-like" name="mostlike" class="form-control" required>
           <option disabled selected value>Select an option</option>
           <option value="challenges">Challenges</option>
           <option value="projects">projects</option>
           <option value="community">community</option>
           <option value="opensource">opensource</option>
          </select>
       </div>

       <div class="form group">
         <p>
           "What Would you like to see improved?"
           <span class="clue">(Check all that apply)</span>
         </p>
         <label>
           <input name="prefer" value="front-end-projects" type="checkbox" class="input-checkbox">
           "Front-end-Projects"
         </label>
         <label>
           <input name="prefer" value="back-end-projects" type="checkbox" class="input-checkbox">
           "Back-end-Projects"
         </label>
         <label>
           <input name="prefer" value="data-visualization" type="checkbox" class="input-checkbox">
           "Data-visualization"
         </label>
         <label>
           <input name="prefer" value="challenges" type="checkbox" class="input-checkbox">
           "challenges"
         </label>
         <label>
           <input name="prefer" value="open-source-community" type="checkbox" class="input-checkbox">
           "open-source-community"
         </label>
         <label>
           <input name="prefer" value="gitter-help-rooms" type="checkbox" class="input-checkbox">
           "gitter-help-rooms"
         </label>
         <label>
           <input name="prefer" value="videos" type="checkbox" class="input-checkbox">
           "Videos"
         </label>
         <label>
           <input name="prefer" value="city-meetups" type="checkbox" class="input-checkbox">
           "city-meetups"
         </label>
         <label>
           <input name="prefer" value="wiki" type="checkbox" class="input-checkbox">
           "wiki"
         </label>
         <label>
           <input name="prefer" value="forum" type="checkbox" class="input-checkbox">
           "forum"
         </label>
         <label>
           <input name="prefer" value="additional-courses" type="checkbox" class="input-checkbox">
           "additional-courses"
         </label>
       </div>
      <div class="form-group">
        <p>Any comments or suggestions?</p>
        <textarea id="comments" class="input-textarea" name="comments" placeholder="Enter your comment here..."></textarea>
        </div>
      <div class="form-group">
        <input type="submit" id="submit" value="Submit">
        </div>
     </form>
    </div>
  </body>
 </html>
