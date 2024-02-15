# Function for inserting tasks

def insert_task():
    
    task=input("Enter your task to be sheduled.\n")
    
    tasks_list.append(task)
    
    print("Task inserted successfully.\n")

    print("\n---------------------------------------------------------------\n--------------------------------------------------------------\n")

#Function for viewing tasks

def view_task():
    
    if len(tasks_list)==0:
        
        print("Task shedule empty!")
    
    else:
        
        for i,task in enumerate(tasks_list):
            
            print(f'{1+i}.{task}')

    print("\n---------------------------------------------------------------\n--------------------------------------------------------------\n")

#Function for deleting tasks

def delete_task():
    
    if len(tasks_list)==0:
        
        print("Task shedule empty!")
    
    else:
        
        for i,task in enumerate(tasks_list):
            
            print(f'{1+i}.{task}')
       
        choice=int(input("Enter which task number to delete the task\n"))
        
        tasks_list.remove(tasks_list[choice-1])
        
        print("Task deleted Succusfully")

    print("\n---------------------------------------------------------------\n--------------------------------------------------------------\n")

#declaring global variable task_list for storing,viewing and deleting tasks of user       

tasks_list=[]

print("---------W-E-L-L-C-O-M-E---T-O---Y-O-U-R---S-H-E-D-U-L-E---------\n\n")

while True:
    
    print("Enter your choice to do the any one from the following")
    
    print("1.Insert Task\n2.View Task\n3.Delete Task\n4.Quit")
    
    choice=int(input())
    
    if choice==1:
        
        insert_task()   #factipon call
    
    elif choice==2:
        
        view_task()      #factipon call   
    
    elif choice==3:
        
        delete_task()       #factipon call
    
    elif choice==4:
        
        print("********hank you for your activeness**********")
        
        break #terminatring loop after clicking quit option by user
    
    else:
       
       print("enter valid option")
