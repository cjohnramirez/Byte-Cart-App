import { useState } from "react";
import { ChevronDown, Heart, ShoppingCart, User } from "react-feather";

interface NavBarProps {
  navComponents: { name: string; linkId: string }[];
}

export default function NavBar(props: NavBarProps) {
  const [openDepartment, setOpenDepartment] = useState<boolean>(false);

  const [selectedDepartment, setSelectedDepartment] = useState<string>("All");

  const departments: string[] = ["Gadgets", "Clothing", "Sports", "Power"];

  const features: {
    featureName: string;
    featureIcon: React.ReactNode;
    featureLink: string;
  }[] = [
    {
      featureName: "LikedItems",
      featureIcon: <Heart />,
      featureLink: "",
    },
    {
      featureName: "Cart",
      featureIcon: <ShoppingCart />,
      featureLink: "",
    },
    {
      featureName: "Profile",
      featureIcon: <User />,
      featureLink: "",
    },
  ];

  const { navComponents } = props;

  console.log(openDepartment);

  return (
    <div className="flex items-center justify-between gap-10 py-4 px-6">
      <div className="flex items-center gap-10">
        <h1 className="text-3xl font-bold">ByteCart</h1>
        {navComponents.map((component) => (
          <a key={component.name} href={component.linkId}>
            {component.name}
          </a>
        ))}
      </div>
      <div className="flex items-center gap-5">
        <div className="flex gap-4 rounded-lg border-2 border-black px-4 py-2">
          <p>{selectedDepartment}</p>
          <div className="relative flex">
            <button
              onClick={() => {
                setOpenDepartment(!openDepartment);
              }}
            >
              <ChevronDown />
            </button>
            <ul
              className={
                (openDepartment ? "block" : "hidden") +
                " absolute -left-[92px] top-10 rounded-md border-2 border-black bg-white p-2"
              }
            >
              {departments.map((department, index) => (
                <li className="rounded-md px-4 hover:bg-gray-300" key={index}>
                  <button
                    key={department}
                    onClick={() => {
                      setSelectedDepartment(department);
                      setOpenDepartment(!openDepartment);
                    }}
                  >
                    {department}
                  </button>
                </li>
              ))}
            </ul>
          </div>
          <input type="text" placeholder="Search"></input>
        </div>
        <button className="button px-4">Sell Your Item</button>
        <div className="py-4 flex">
          {features.map((feature) => (
            <a
              className="pl-4"
              key={feature.featureName}
              href={feature.featureLink}
            >
              {feature.featureIcon}
            </a>
          ))}
        </div>
      </div>
    </div>
  );
}
