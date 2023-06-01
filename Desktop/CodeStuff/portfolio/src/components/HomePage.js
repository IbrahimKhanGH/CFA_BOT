import React from 'react';

const HomePage = () => {
  return (
    <div className="bg-gray-100 min-h-screen">
      <header className="bg-white shadow">
        <div className="container mx-auto px-4 py-6 flex items-center justify-between">
          <h1 className="text-2xl font-bold">My Portfolio</h1>
          <nav>
            <ul className="flex space-x-4">
              <li><a href="#" className="text-gray-700 hover:text-gray-900">Home</a></li>
              <li><a href="#" className="text-gray-700 hover:text-gray-900">About</a></li>
              <li><a href="#" className="text-gray-700 hover:text-gray-900">Projects</a></li>
              <li><a href="#" className="text-gray-700 hover:text-gray-900">Contact</a></li>
            </ul>
          </nav>
        </div>
      </header>

      <section className="container mx-auto px-4 py-10">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-white shadow-lg p-6">
            <h2 className="text-2xl font-bold mb-4">About Me</h2>
            <p className="text-gray-700">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum blandit lacinia.
              Fusce nec dolor vitae justo maximus fermentum non eu lorem.
            </p>
          </div>
          <div className="bg-white shadow-lg p-6">
            <h2 className="text-2xl font-bold mb-4">My Projects</h2>
            <ul className="list-disc list-inside text-gray-700">
              <li>Project 1 commit</li>
              <li>Project 2 commit</li>
              <li>Project 3</li>
            </ul>
          </div>
        </div>
      </section>

      <footer className="bg-gray-200 py-4 text-center">
        <p className="text-gray-700">© 2023 My Portfolio. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default HomePage;
