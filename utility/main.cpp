#include <curl/curl.h>
#include <fstream>
#include <iostream>
#include <string>
#include <sys/stat.h>
#include <vector>

// Function prototypes
void getLinks(std::vector<std::string>&, std::string);
std::string getImageEnd(std::string);

int main(int argc, char** argv) {
	if (argc != 2) {
		std::cout << "Must enter one file with all the links, separated by a newline." << '\n';
	}

	// Directory for images to be saved
	mkdir("tama_images", 0777);
	
	// Init
	CURL *curl;
	CURLcode res;
	bool error = false;

	// Gets links
	std::string fileName = argv[1];
	std::vector<std::string> links;
	getLinks(links, fileName);

	// Save files
	for (int i = 0; i < links.size(); i++) {
		FILE *pagefile;
		std::string newFileName = "tama_images/" + getImageEnd(links[i]);

		// Check for conflicts
		std::ifstream file(newFileName);
		if (file.good()) {
			std::cout << "Conflict found for: " + links[i] << '\n';
			continue;
		}

		pagefile = fopen(newFileName.c_str(), "wb");

		curl = curl_easy_init();
		curl_easy_setopt(curl, CURLOPT_URL, links[i].c_str());
		curl_easy_setopt(curl, CURLOPT_WRITEDATA, pagefile);
		curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1);
		res = curl_easy_perform(curl);

		// Clean up
		curl_easy_cleanup(curl);
		fclose(pagefile);

		if (res != 0) {
			error = true;
		}
	}

	// Error reporting
	if (error) {
		std::cout << "Error has occured" << '\n';
	}

	return 0;
}

void getLinks(std::vector<std::string>& strVec, std::string fileName) {
	std::ifstream file(fileName);
	std::string input;

	file >> input;
	while (!file.eof()) {
		strVec.push_back(input);
		file >> input;
	}
}

std::string getImageEnd(std::string link) {
	int found = link.find_last_of("/");
	return link.substr(found + 1);
}

