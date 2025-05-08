from commands import handle_command

def main () :
    print ("File explorer (CLI based)")
    print("Type 'help' to see available commands")
    while True :
      try :
         command = input("file-explorer> ").strip()
         if command in ("exit" , "quit"):
            print ("exiting file explorer")
            break
         handle_command(command)
      except KeyboardInterrupt:
         print("\nUse 'exit' to quit ")
      except Exception as e:
         print(f"Error: {e}")

if __name__ == "__main__":
   main()
  