# -*- coding: utf-8 -*-
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from numpy import*
import sys

M_translate_x_right = matrix('1.0 0.0 10.0; 0.0 1.0 0.0; 0.0 0.0 1.0')
M_translate_x_left = matrix('1.0 0.0 -10.0; 0.0 1.0 0.0; 0.0 0.0 1.0')
M_translate_y_up = matrix('1.0 0.0 0.0; 0.0 1.0 10.0; 0.0 0.0 1.0')
M_translate_y_down = matrix('1.0 0.0 0.0; 0.0 1.0 -10.0; 0.0 0.0 1.0')


pravoagolnik = matrix('30.0 30.0 50.0 50.0;540.0 560.0 560.0 540.0;1.0 1.0 1.0 1.0')#Main Character
pravoagolnikStart = matrix('30.0 30.0 50.0 50.0;540.0 560.0 560.0 540.0;1.0 1.0 1.0 1.0')#Start position of the main character
#Barriers
prepreka1 = matrix('0.0 0.0 20.0 20.0; 0.0 600.0 600.0 0.0')
prepreka2 = matrix('60.0 60.0 180.0 180.0; 520.0 600.0 600.0 520.0')
prepreka3 = matrix('0.0 0.0 600.0 600.0; 580.0 600.0 600.0 580.0')
prepreka4 = matrix('0.0 0.0 220.0 220.0; 320.0 480.0 480.0 320.0')
prepreka5 = matrix('220.0 220.0 540.0 540.0; 400.0 540.0 540.0 400.0')
prepreka6 = matrix('580.0 580.0 600.0 600.0; 0.0 600.0 600.0 0.0')
prepreka7 = matrix('60.0 60.0 260.0 260.0; 220.0 280.0 280.0 220.0')
prepreka8 = matrix('260.0 260.0 580.0 580.0; 160.0 360.0 360.0 160.0')
prepreka9 = matrix('0.0 0.0 220.0 220.0; 0.0 160.0 160.0 0.0')
prepreka10 = matrix('220.0 220.0 560.0 560.0; 0.0 140.0 140.0 0.0')
prepreka11 = matrix('560.0 560.0 580.0 580.0; 0.0 20.0 20.0 0.0')


#Drawing of map and main character
def mapAndMainCharacter():   
     glClear(GL_COLOR_BUFFER_BIT)  
     glPointSize(4.0)

     glBegin(GL_POLYGON)
     glColor3f(0.000, 0.000, 0.804)
     glVertex2f(pravoagolnik.item(0), pravoagolnik.item(4))
     glVertex2f(pravoagolnik.item(1), pravoagolnik.item(5))
     glVertex2f(pravoagolnik.item(2), pravoagolnik.item(6))
     glVertex2f(pravoagolnik.item(3), pravoagolnik.item(7))
     glEnd()

     glBegin(GL_POLYGON)
     glColor3f(0.0, 0.0, 0.0,)
     glVertex2f(prepreka1.item(0), prepreka1.item(4))
     glVertex2f(prepreka1.item(1), prepreka1.item(5))
     glVertex2f(prepreka1.item(2), prepreka1.item(6))
     glVertex2f(prepreka1.item(3), prepreka1.item(7))
     glEnd()

     glBegin(GL_POLYGON)
     glColor3f(0.0, 0.0, 0.0,)
     glVertex2f(prepreka2.item(0), prepreka2.item(4))
     glVertex2f(prepreka2.item(1), prepreka2.item(5))
     glVertex2f(prepreka2.item(2), prepreka2.item(6))
     glVertex2f(prepreka2.item(3), prepreka2.item(7))
     glEnd()

     glBegin(GL_POLYGON)
     glColor3f(0.0, 0.0, 0.0,)
     glVertex2f(prepreka3.item(0), prepreka3.item(4))
     glVertex2f(prepreka3.item(1), prepreka3.item(5))
     glVertex2f(prepreka3.item(2), prepreka3.item(6))
     glVertex2f(prepreka3.item(3), prepreka3.item(7))
     glEnd()

     glBegin(GL_POLYGON)
     glColor3f(0.0, 0.0, 0.0,)
     glVertex2f(prepreka4.item(0), prepreka4.item(4))
     glVertex2f(prepreka4.item(1), prepreka4.item(5))
     glVertex2f(prepreka4.item(2), prepreka4.item(6))
     glVertex2f(prepreka4.item(3), prepreka4.item(7))
     glEnd()

     glBegin(GL_POLYGON)
     glColor3f(0.0, 0.0, 0.0,)
     glVertex2f(prepreka5.item(0), prepreka5.item(4))
     glVertex2f(prepreka5.item(1), prepreka5.item(5))
     glVertex2f(prepreka5.item(2), prepreka5.item(6))
     glVertex2f(prepreka5.item(3), prepreka5.item(7))
     glEnd()
     
     glBegin(GL_POLYGON)
     glColor3f(0.0, 0.0, 0.0,)
     glVertex2f(prepreka6.item(0), prepreka6.item(4))
     glVertex2f(prepreka6.item(1), prepreka6.item(5))
     glVertex2f(prepreka6.item(2), prepreka6.item(6))
     glVertex2f(prepreka6.item(3), prepreka6.item(7))
     glEnd()

     glBegin(GL_POLYGON)
     glColor3f(0.0, 0.0, 0.0,)
     glVertex2f(prepreka7.item(0), prepreka7.item(4))
     glVertex2f(prepreka7.item(1), prepreka7.item(5))
     glVertex2f(prepreka7.item(2), prepreka7.item(6))
     glVertex2f(prepreka7.item(3), prepreka7.item(7))
     glEnd()

     glBegin(GL_POLYGON)
     glColor3f(0.0, 0.0, 0.0,)
     glVertex2f(prepreka8.item(0), prepreka8.item(4))
     glVertex2f(prepreka8.item(1), prepreka8.item(5))
     glVertex2f(prepreka8.item(2), prepreka8.item(6))
     glVertex2f(prepreka8.item(3), prepreka8.item(7))
     glEnd()

     glBegin(GL_POLYGON)
     glColor3f(0.0, 0.0, 0.0,)
     glVertex2f(prepreka9.item(0), prepreka9.item(4))
     glVertex2f(prepreka9.item(1), prepreka9.item(5))
     glVertex2f(prepreka9.item(2), prepreka9.item(6))
     glVertex2f(prepreka9.item(3), prepreka9.item(7))
     glEnd()

     glBegin(GL_POLYGON)
     glColor3f(0.0, 0.0, 0.0,)
     glVertex2f(prepreka10.item(0), prepreka10.item(4))
     glVertex2f(prepreka10.item(1), prepreka10.item(5))
     glVertex2f(prepreka10.item(2), prepreka10.item(6))
     glVertex2f(prepreka10.item(3), prepreka10.item(7))
     glEnd()

     glBegin(GL_POLYGON)
     glColor3f(0.863, 0.078, 0.235)
     glVertex2f(prepreka11.item(0), prepreka11.item(4))
     glVertex2f(prepreka11.item(1), prepreka11.item(5))
     glVertex2f(prepreka11.item(2), prepreka11.item(6))
     glVertex2f(prepreka11.item(3), prepreka11.item(7))
     glEnd()

     
     glFlush()


#VictoryEvent
def display():
     glClear(GL_COLOR_BUFFER_BIT)  
     glPointSize(4.0)
     glBegin(GL_POINTS)
     glColor3f(0.2, 0.8, 0.1)
     
#W
     t=0
     for w in arange(100.0, 160, 1):
          a=450-t
          t=t+2
          glVertex2f(w, a)
     for w in arange(160.0, 200.0, 1):
          a=210+t
          t=t+2
          glVertex2f(w, a)
     for w in arange(200.0, 240.0, 1):
          a=610-t
          t=t+2
          glVertex2f(w, a)
     for w in arange(240.0, 300.0, 1):
          a=50+t
          t=t+2
          glVertex2f(w, a)

     #I
     x1= 350.0
     for i in arange(332.0, 450.0, 1):
          glVertex2f(x1, i)

     #N
     x2= 400.0
     t=0
     for n in arange(332.0, 450.0, 1):
          glVertex2f(x2, n)
     for n in arange(400.0, 460.0, 1):
          a=450-t
          t=t+2
          glVertex2f(n, a)
     for n in arange(332.0, 450.0, 1):
          glVertex2f(x2+60, n)

     glEnd()
     glFlush()


#Movement and restarting when hit a barrier
def transformations (key, x, y):
     global pravoagolnik
     if key == 'd':
          pravoagolnik = M_translate_x_right * pravoagolnik
          glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
          mapAndMainCharacter()
     if key == 'a':
          pravoagolnik = M_translate_x_left * pravoagolnik
          glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
          mapAndMainCharacter()
     if key == 'w':
          pravoagolnik = M_translate_y_up * pravoagolnik
          glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
          mapAndMainCharacter()
     if key == 's':
          pravoagolnik = M_translate_y_down * pravoagolnik
          glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
          mapAndMainCharacter()
#Barriers

     #Barrier 1
     for t in arange(0.0, 600.0, 1):
          y=t-10
          if pravoagolnik.item(0) == prepreka1.item(2)-10 and pravoagolnik.item(4) == y:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 2[LEFT]
     for t in arange(520.0, 600.0, 1):
          y=t+10
          if pravoagolnik.item(2) == prepreka2.item(0)+10 and pravoagolnik.item(6) == y:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()
               
     #Barrier 2[DOWN]
     for t in arange(60.0, 180.0, 1):
          x=t
          if pravoagolnik.item(5) == prepreka2.item(4)+10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 2[RIGHT]
     for t in arange(520.0, 600.0, 1):
          y=t+10
          if pravoagolnik.item(0) == prepreka2.item(2)-10 and pravoagolnik.item(5) == y:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()
               
     #Barrier 3
     for t in arange(0.0, 600.0, 1):
          x=t
          if pravoagolnik.item(5) == prepreka3.item(4)+10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 4[TOP and BOTTOM]
     for t in arange(0.0, 220.0, 1):
          x=t
          if pravoagolnik.item(4) == prepreka4.item(5)-10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()
          if pravoagolnik.item(5) == prepreka4.item(4)+10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 4[RIGHT]
     for t in arange(320.0, 400.0, 1):
          y=t+10
          if pravoagolnik.item(0) == prepreka4.item(3)-10 and pravoagolnik.item(5) == y:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()



     #Barrier 5[LEFT]
     for t in arange(480.0, 540.0, 1):
          y=t+20
          if pravoagolnik.item(3) == prepreka5.item(0)+10 and pravoagolnik.item(6) == y:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()


     #Barrier 5[TOP and BOTTOM]
     for t in arange(220.0, 540.0, 1):
          x=t
          if pravoagolnik.item(4) == prepreka5.item(5)-10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()
          if pravoagolnik.item(5) == prepreka5.item(4)+10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 5[RIGHT]
     for t in arange(400.0, 540.0, 1):
          y=t+10
          if pravoagolnik.item(0) == prepreka5.item(3)-10 and pravoagolnik.item(5) == y:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 6
     for t in arange(0.0, 600.0, 1):
          y=t+10
          if pravoagolnik.item(3) == prepreka6.item(0)+10 and pravoagolnik.item(6) == y:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 7[TOP and BOTTOM]
     for t in arange(60.0, 260.0, 1):
          x=t
          if pravoagolnik.item(4) == prepreka7.item(5)-10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()
          if pravoagolnik.item(5) == prepreka7.item(4)+10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 7[LEFT]
     for t in arange(220.0, 280.0, 1):
          y=t+20
          if pravoagolnik.item(3) == prepreka7.item(0)+10 and pravoagolnik.item(6) == y-10:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 8[TOP and BOTTOM]
     for t in arange(260.0, 600.0, 1):
          x=t
          if pravoagolnik.item(4) == prepreka8.item(5)-10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()
          if pravoagolnik.item(5) == prepreka8.item(4)+10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 8[LEFT]
     for t in arange(160.0, 360.0, 1):
          y=t+20
          if pravoagolnik.item(3) == prepreka8.item(0)+10 and pravoagolnik.item(6) == y-10:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 9[TOP]
     for t in arange(0.0, 220.0, 1):
          x=t
          if pravoagolnik.item(4) == prepreka9.item(5)-10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 9[RIGHT]
     for t in arange(120.0, 160.0, 1):
          y=t+10
          if pravoagolnik.item(0) == prepreka9.item(3)-10 and pravoagolnik.item(5) == y:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 10[TOP]
     for t in arange(160.0, 560.0, 1):
          x=t
          if pravoagolnik.item(4) == prepreka10.item(5)-10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()

     #Barrier 10[RIGHT]
     for t in arange(0.0, 140.0, 1):
          y=t+10
          if pravoagolnik.item(0) == prepreka10.item(3)-10 and pravoagolnik.item(5) == y:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               mapAndMainCharacter()
               

     #Victory
     for t in arange(560.0, 580.0, 1):
          x=t
          if pravoagolnik.item(4) == prepreka11.item(5)-10 and pravoagolnik.item(1) == x:
               pravoagolnik = pravoagolnikStart
               glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
               display()
        

def initWindow():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Maze Game-BETA")
    glutDisplayFunc(display)
    glutDisplayFunc(mapAndMainCharacter)
    glutKeyboardFunc(transformations)
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(0.0, 600.0, 0.0, 600.0)
    
initWindow()
glutMainLoop()
