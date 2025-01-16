function App() {
  //Type annotation
  function greet(person: string, date: Date) {
    console.log(`Hello ${person}, today is ${date.toDateString()}!`)
  }

  greet("jcr", new Date())

  //TypeScript does this automatically if variable is initialized in a specific data type
  let myName: string = "jcr"
  //is the same to myName = "jcr" 

  //Type annotation for return value of functions
  function getFavoriteNumber(): number {
    return 26
  }

  //Type annotation for return value of asynchronous function 
  async function getNumber(): Promise<number> {
    return 26;
  }

  const names = ["wow"]

  //type annotation for anonymous functions are based on context
  names.forEach((s) => {
    console.log(s.toUpperCase())
  })

  //Union Type (note that separators, line breaks are allowed as well)
  function printId(id: number | string) {
    console.log("Your ID is: " + id);
  }

  // OK
  printId(101);
  // OK
  printId("202");
  // Error printId({ myID: 22342 });

  //Type Aliases, preferred if a certain group of code elements has the same properties to avoid duplication / for refactoring
  type Point = {
    x: number;
    y: number;
  }

  function printCoord(pt: Point) {
    console.log("The coordinate's x value is " + pt.x);
    console.log("The coordinate's y value is " + pt.y);
  }
  printCoord({ x: 100, y: 100 });

  //Almost the same with Type Aliases
  interface User {
    name: string,
    age: number
  }

  function printUser(user: User) {
    console.log("The user is " + user.name + " aged " + user.age)
  }

  //Difference with type aliases and interface is that the latter can create new fields at will, while the former cannot (although both can extend a type)

  //Type Assertions
  const myCanvas = document.getElementById("main_canvas") as HTMLCanvasElement;

  //You can combine unions with literals (legit an amazing feature by TypeScript AHAHAHAHA)
  let positions: "left" | "right" | "down" | "up" 
  positions = "right" 

  return (
    <>
      <h1 className="text-3xl font-bold">ByteCart</h1>
    </>
  )
}

export default App
