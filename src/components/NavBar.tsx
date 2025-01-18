interface NavBarProps {
  navComponents : { name: string; linkId: string }[];
}

export default function NavBar(props : NavBarProps) {
  const departments : string[] = ["Gadgets", "Clothing", "Sports", "Power"]
  const { navComponents } = props

  return (
    <div>
      <h1 className="text-3xl font-bold">ByteCart</h1>
      {navComponents.map((component) => (
        <a key={component.name} href={component.linkId}>{component.name}</a>
      ))}
      <div>
        <div>
          
          <i className="fa-solid fa-chevron-down"></i>
        </div>
        <input type="text" placeholder="Search"/>
      </div>
      
    </div>
  )
}