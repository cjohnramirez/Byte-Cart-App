import { useState } from "react";

interface NavBarProps {
  navComponents: { name: string; linkId: string }[];
}

export default function NavBar(props: NavBarProps) {
  const [openDepartment, setOpenDepartment] = useState<boolean>(false);

  const [selectedDepartment, setSelectedDepartment] = useState<string>("All");

  const departments: string[] = ["Gadgets", "Clothing", "Sports", "Power"];

  const features: {
    featureName: string;
    featureIcon: string;
    featureLink: string;
  }[] = [
    {
      featureName: "LikedItems",
      featureIcon: "fa-solid fa-heart",
      featureLink: "",
    },
    {
      featureName: "Cart",
      featureIcon: "fa-solid fa-cart-shopping",
      featureLink: "",
    },
    {
      featureName: "Profile",
      featureIcon: "fa-solid fa-user",
      featureLink: "",
    },
  ];

  const { navComponents } = props;

  console.log(openDepartment);

  return (
    <div className="flex items-center p-4 gap-10">
      <div className="flex justify-between items-center w-1/2">
        <h1 className="text-3xl font-bold">ByteCart</h1>
        {navComponents.map((component) => (
          <a key={component.name} href={component.linkId}>
            {component.name}
          </a>
        ))}
      </div>
      <div className="flex justify-between items-center w-1/2">
        <div className="flex items-center border-black border-2 rounded-full px-4 py-2">
          <p>{selectedDepartment}</p>
          <div className="relative inline-block">
            <button onClick={() => {
              setOpenDepartment(!openDepartment)
            }}>
              <i className="fa-solid fa-chevron-down"></i>
            </button>
            <ul
              className={
                (openDepartment ? "block" : "hidden") +
                " absolute bg-white rounded-lg shadow-md p-4"
              }
            >
              {departments.map((department) => (
                <li className="hover:bg-gray-300">
                  <button key={department} onClick={() => {
                    setSelectedDepartment(department)
                    setOpenDepartment(!openDepartment)
                    }}>{department}</button>
                </li>
              ))}
            </ul>
          </div>
          <input type="text" placeholder="search"></input>
        </div>
        <button className="border-black border-2 rounded-full px-4 py-2">Sell Your Item</button>
        <div className="p-4">
          {features.map((feature) => (
            <a key={feature.featureName} href={feature.featureLink}>
              <i className={feature.featureIcon}></i>
            </a>
          ))}
        </div>
      </div>
    </div>
  );
}
