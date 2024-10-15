import tkinter as tk

#WINDOW
w = tk.Tk()
w.title(210*" "+ "Sentiment Analysis of Tweets")
w.config(bg="White")

#TEXT BOX
text1=tk.Text(w,height=5)
font30 = ("Arihona",30,"bold")
# Add the tag in the given text
text1.tag_add("heading", "1.0")
#change font and alignment
text1.tag_config("heading",font=font30,justify="center",foreground="Maroon")
# Insert content
text1.insert("1.0","Perform Sentiment Analysis","heading")
# Position the text
text1.pack(fill="x",padx=0,pady=0)

#TOPIC DISPLAY
text2=tk.Text(w,height=5)
font20 = ("Arihona",20,"bold")
#add tag to the text
text2.tag_add("topic", "1.0")
#change font and alignment
text2.tag_config("topic",font=font20,justify="center",foreground="Orange")
# Insert content
text2.insert("1.0", "Choose a topic","topic")
# Position text
text2.pack(fill="x",padx=0,pady=0)

#FUNCTION TO EXECUTE AFTER CLICKING BUTTON
def changetextb1():
    text2.delete(1.0,"end")
    text2.insert(1.0,b1['text'],"topic")
    b1['text'] = "Topic chosen !"
    
    
def changetextb2():
    text2.delete(1.0,"end")
    text2.insert(1.0,b2['text'],"topic")
    b2['text'] = "Topic chosen !"   
    
def changetextb3():
    text2.delete(1.0,"end")
    text2.insert(1.0,b3['text'],"topic")
    b3['text'] = "Topic chosen !" 

                     
#BUTTONS TO CHOOSE TOPICS
b1=tk.Button(w,text="#hash1",background="dark green",foreground="white",command=changetextb1)
b1.pack(padx=10,pady=10)

b2=tk.Button(w,text="#hash2",background="dark green",foreground="white",command=changetextb2)
b2.pack(padx=10,pady=10)

b3=tk.Button(w,text="#hash3",background="dark green",foreground="white",command=changetextb3)
b3.pack(padx=10,pady=10)


#Analysis result must be shown at bottom
text3=tk.Text(w,height=5)
font10 = ("Arihona",10,"bold")
#add tag to the text
text3.tag_add("analysis", "1.0")
#change font and alignment
text3.tag_config("analysis",font=font10,justify="center",foreground="blue")
# Insert content
text3.insert("1.0", "analysis results are shown below","analysis")
# Position text
text3.pack(fill="x",padx=0,pady=0)

#MAINLOOP
w.mainloop()
