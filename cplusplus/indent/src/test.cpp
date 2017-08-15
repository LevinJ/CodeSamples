/*
 * particle_filter.cpp
 *
 *  Created on: Dec 12, 2016
 *      Author: Tiffany Huang
 */

#include <random>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <math.h>
#include <iostream>
#include <sstream>
#include <string>
#include <iterator>
#include <map>

#include "particle_filter.h"

using namespace std;

void ParticleFilter::init(double x, double y, double theta, double std[]) {
	// TODO: Set the number of particles. Initialize all particles to first position (based on estimates of
	//   x, y, theta and their uncertainties from GPS) and all weights to 1.
	// Add random Gaussian noise to each particle.
	// NOTE: Consult particle_filter.h for more information about this method (and others in this file).
	num_particles = 50;

	std::default_random_engine gen;

	std::normal_distribution<double> N_x(x, std[0]);
	std::normal_distribution<double> N_y(x, std[1]);
	std::normal_distribution<double> N_theta(theta, std[2]);

	for(int ii = 0; ii< num_particles; ii++){
		Particle particle;
		particle.id = ii;
		particle.x = N_x(gen);
		particle.y = N_y(gen);
		particle.theta = N_theta(gen);
		particle.weight = 1.0;

		particles.push_back(particle);
		weights.push_back(1.0);
	}
	is_initialized = true;
}

void ParticleFilter::prediction(double delta_t, double std_pos[], double velocity, double yaw_rate) {
	// TODO: Add measurements to each particle and add random Gaussian noise.
	// NOTE: When adding noise you may find std::normal_distribution and std::default_random_engine useful.
	//  http://en.cppreference.com/w/cpp/numeric/random/normal_distribution
	//  http://www.cplusplus.com/reference/random/default_random_engine/

	//cout << "prediction start" << endl;

	default_random_engine gen;

	normal_distribution<double> N_x(0.0, std_pos[0]);
	normal_distribution<double> N_y(0.0, std_pos[1]);
	normal_distribution<double> N_theta(0.0, std_pos[2]);

	double tol = 1e-5;

	for(int ii = 0; ii< num_particles; ii++){
		double new_x;
		double new_y;
		double new_theta;

		if(fabs(yaw_rate) < tol){
			particles[ii].x = particles[ii].x + velocity*delta_t*cos(particles[ii].theta) + N_x(gen);
			particles[ii].y = particles[ii].y + velocity*delta_t*sin(particles[ii].theta) + N_y(gen);
			particles[ii].theta = particles[ii].theta + + N_theta(gen);
		} else {
			particles[ii].x =
					particles[ii].x + velocity/yaw_rate*(sin(particles[ii].theta+yaw_rate*delta_t)-sin(particles[ii].theta)) + N_x(gen);
			particles[ii].y = particles[ii].y + velocity/yaw_rate*(cos(particles[ii].theta)-cos(particles[ii].theta+yaw_rate*delta_t)) + N_y(gen);
			particles[ii].theta = particles[ii].theta + yaw_rate*delta_t + N_theta(gen);
		}

	}

	//cout << "prediction end" << endl;
}

void ParticleFilter::dataAssociation(std::vector<LandmarkObs> predicted, std::vector<LandmarkObs>& observations) {
	// TODO: Find the predicted measurement that is closest to each observed measurement and assign the
	//   observed measurement to this particular landmark.
	// NOTE: this method will NOT be called by the grading code. But you will probably find it useful to
	//   implement this method and use it as a helper during the updateWeights phase.
}
void dataAssociationPerParticle(std::vector<LandmarkObs>& predicted, const std::vector<LandmarkObs> &observations) {

    std::vector<LandmarkObs> predicted_mapped;

    for (auto &iter_Observed: observations) {
        double shortest_dist = INFINITY;

        // the predicted measurement that is closest to each observed measurement
        LandmarkObs closestLandmark;

        for (auto iter_Predicted: predicted) {
            // compute distance between observed & predicted measurements
            double cur_dist = dist(iter_Observed.x,  iter_Observed.y,
                                   iter_Predicted.x, iter_Predicted.y);
            // if new distance is minimal then remember it in shortest_dist
            if (cur_dist < shortest_dist) {
                shortest_dist = cur_dist;
                closestLandmark = iter_Predicted;
            }
        }

        // store the new found nearest landmark
        predicted_mapped.push_back(closestLandmark);
    }
    predicted = predicted_mapped;
}

void ParticleFilter::updateWeights(double sensor_range, double std_landmark[],
		std::vector<LandmarkObs> observations, Map map_landmarks) {
	 	 weights.resize(num_particles, 1.0);

	    const double std_x = std_landmark[0];
	    const double std_y = std_landmark[1];

	    // avoid repeating numeric expressions, taking computation out of loop
	    const double two_std_x_sqrd = 2. * std_x * std_x;
	    const double two_std_y_sqrd = 2. * std_y * std_y;
	    const double two_Pi_std_x_std_y = 2. * M_PI * std_x * std_y;

	    std::vector<LandmarkObs> observations_p = observations;
	    for (int i = 0; i < particles.size(); ++i) {

	        Particle &p = particles[i];

	        // transform each observation coordinates from vehicle XY to map XY system
	        for (int j=0; j< observations_p.size(); j++) {
	        	double x =p.x + observations_p[j].x * cos(p.theta) - observations_p[j].y * sin(p.theta);
	        	double y =p.y + observations_p[j].x * sin(p.theta) + observations_p[j].y * cos(p.theta);
	        	observations[j].x = x;
	        	observations[j].y = y;
	        }

	        vector<LandmarkObs> predicted_landmarks;
	        for (auto iterLandmark: map_landmarks.landmark_list) {

				LandmarkObs landmark;
				landmark.id = iterLandmark.id_i;
				landmark.x = iterLandmark.x_f;
				landmark.y = iterLandmark.y_f;
				predicted_landmarks.push_back(landmark);
	        }


	        dataAssociationPerParticle(predicted_landmarks, observations);
	        // compute weights for the closest landmarks
	        double wt = 1.0;
	        for (int j = 0; j < predicted_landmarks.size(); ++j) {
	            double dx = observations[j].x - predicted_landmarks[j].x;
	            double dy = observations[j].y - predicted_landmarks[j].y;

	            wt *= 1.0 / (two_Pi_std_x_std_y) * exp(-dx * dx / (two_std_x_sqrd)) * exp(-dy * dy / (two_std_y_sqrd));

	            // update stored values of the particle & filter weigths
	            weights[i] = p.weight = wt;
	        }
	    }
}
/*
void ParticleFilter::updateWeights(double sensor_range, double std_landmark[],
		std::vector<LandmarkObs> observations, Map map_landmarks) {

	//cout << "update start" << endl;
	// TODO: Update the weights of each particle using a mult-variate Gaussian distribution. You can read
	//   more about this distribution here: https://en.wikipedia.org/wiki/Multivariate_normal_distribution
	// NOTE: The observations are given in the VEHICLE'S coordinate system. Your particles are located
	//   according to the MAP'S coordinate system. You will need to transform between the two systems.
	//   Keep in mind that this transformation requires both rotation AND translation (but no scaling).
	//   The following is a good resource for the theory:
	//   https://www.willamette.edu/~gorr/classes/GeneralGraphics/Transforms/transforms2d.htm
	//   and the following is a good resource for the actual equation to implement (look at equation
	//   3.33
	//   http://planning.cs.uiuc.edu/node99.html
	for(int ii=0; ii<num_particles; ii++) {

		//cout << "loop count " << ii << endl;
		vector<LandmarkObs> copy_observations = observations;


		//cout << "trans before" << endl;
		for(int kk=0; kk<copy_observations.size();kk++){
			transParticle2MapCoodinate(copy_observations[kk], particles[ii]);
		}
		//cout << "trans end" << endl;

		// obtain a list of landmarks which are in sensor range
		vector<LandmarkObs> landmark_in_range;
		std::map<int, Map::single_landmark_s> mappingLandmarks;

		//cout << "landmark range before" << endl;
		for(int kk=0; kk<map_landmarks.landmark_list.size(); kk++){
			Map::single_landmark_s lan = map_landmarks.landmark_list[kk];
			double distance = dist(lan.x_f, lan.y_f, particles[ii].x, particles[ii].y);
			if (distance <= sensor_range)
			{
				landmark_in_range.push_back(LandmarkObs{lan.id_i,lan.x_f,lan.y_f});
				// log the landmark so that it can be used later
				mappingLandmarks.insert(make_pair(lan.id_i, lan));
			}
		}
		//cout << "landmark range end" << endl;

		//cout << "update sensor range landmark" << endl;

		if(landmark_in_range.size() > 0){
			//cout << "association before" << endl;

			for(int kk=0; kk<copy_observations.size(); kk++) {
				vector<double> distances;

				for (int ll=0; ll<landmark_in_range.size(); ll++){
					double dist_val = dist(copy_observations[kk].x, copy_observations[kk].y,
							landmark_in_range[ll].x, landmark_in_range[ll].y);
					distances.push_back(dist_val);
				}

				int id = distance(distances.begin(),min_element(distances.begin(),distances.end()));
				copy_observations[kk].id = landmark_in_range[id].id;
			}
			//cout << "association end" << endl;

			//cout << "update associated landmark id" << endl;

			vector<double> weights;

			weights = calculateWeights(particles[ii], copy_observations, std_landmark, mappingLandmarks);
			particles[ii].weight = accumulate(weights.begin(),weights.end(),1.0, multiplies<double>());

			//cout << "calc weight end" << endl;

			vector<int> associations;
			vector<double> sense_x;
			vector<double> sense_y;
			// set associations
			for(auto obs: copy_observations){
				associations.push_back(obs.id);
				sense_x.push_back(obs.x);
				sense_y.push_back(obs.y);
			}


			//cout << "set associ before" << endl;
			particles[ii] = SetAssociations(particles[ii], associations, sense_x, sense_y);

			//cout << "set associ end" << endl;

		}

	}
	//cout << "update end" << endl;
}
*/

void ParticleFilter::resample() {
	// TODO: Resample particles with replacement with probability proportional to their weight.
	// NOTE: You may find std::discrete_distribution helpful here.
	//   http://en.cppreference.com/w/cpp/numeric/random/discrete_distribution

	vector<Particle> ptTemp;
	Particle pt2Add;
	vector<double> alpha_weights;

	vector<double> dist_weights(num_particles, 1.0);
	discrete_distribution<int> dist_fun(dist_weights.begin(), dist_weights.end());
	normal_distribution<double> dist(0.5, 0.5);
	default_random_engine gen;

	double mw;
	double beta;
	int index;

	// obtain weights of all particles
	for(int i=0; i<num_particles; i++)
	{
		weights[i] = particles[i].weight;
	}

	alpha_weights = normalize_vector(weights);

	mw = *max_element(alpha_weights.begin(), alpha_weights.end());
	index = dist_fun(gen);
	beta = 0.0;

	for(int i=0; i<num_particles; i++)
	{
		beta += 2.0 * mw * dist(gen);
		while (beta > alpha_weights[index])
		{
			beta -= alpha_weights[index];
			index = (index+1) % num_particles;
		}
		pt2Add = particles[index];
		pt2Add.id = i;
		ptTemp.push_back(pt2Add);
	}

	particles = ptTemp;


}

//function to normalize a vector:
vector<double> ParticleFilter::normalize_vector(vector<double> inputVector){

	//declare sum:
	double sum = 0.0;

	//declare and resize output vector:
	std::vector<double> outputVector ;
	outputVector.resize(inputVector.size());

	//estimate the sum:
	for (unsigned int i = 0; i < inputVector.size(); ++i) {
		sum += inputVector[i];
	}

	//normalize with sum:
	for (unsigned int i = 0; i < inputVector.size(); ++i) {
		outputVector[i] = inputVector[i]/sum ;
	}

	//return normalized vector:
	return outputVector ;
}

Particle ParticleFilter::SetAssociations(Particle particle, std::vector<int> associations, std::vector<double> sense_x, std::vector<double> sense_y)
{
	//particle: the particle to assign each listed association, and association's (x,y) world coordinates mapping to
	// associations: The landmark id that goes along with each listed association
	// sense_x: the associations x mapping already converted to world coordinates
	// sense_y: the associations y mapping already converted to world coordinates

	//Clear the previous associations

	particle.associations.clear();
	particle.sense_x.clear();
	particle.sense_y.clear();

	particle.associations= associations;
	particle.sense_x = sense_x;
	particle.sense_y = sense_y;

	return particle;
}

string ParticleFilter::getAssociations(Particle best)
{
	vector<int> v = best.associations;
	stringstream ss;
	copy( v.begin(), v.end(), ostream_iterator<int>(ss, " "));
	string s = ss.str();
	s = s.substr(0, s.length()-1);  // get rid of the trailing space
	return s;
}
string ParticleFilter::getSenseX(Particle best)
{
	vector<double> v = best.sense_x;
	stringstream ss;
	copy( v.begin(), v.end(), ostream_iterator<float>(ss, " "));
	string s = ss.str();
	s = s.substr(0, s.length()-1);  // get rid of the trailing space
	return s;
}
string ParticleFilter::getSenseY(Particle best)
{
	vector<double> v = best.sense_y;
	stringstream ss;
	copy( v.begin(), v.end(), ostream_iterator<float>(ss, " "));
	string s = ss.str();
	s = s.substr(0, s.length()-1);  // get rid of the trailing space
	return s;
}

void ParticleFilter::transParticle2MapCoodinate(LandmarkObs &obs, Particle particle)
{

	double theta_0 = particle.theta;
	double x_t = particle.x;
	double y_t = particle.y;
	double x = obs.x;
	double y = obs.y;

	obs.x = x*cos(theta_0) - y*sin(theta_0) + x_t;
	obs.y = x*sin(theta_0) + y*cos(theta_0) + y_t;

}

vector<double> ParticleFilter::calculateWeights(Particle particle, vector<LandmarkObs> observations, double std_landmark[], map<int, Map::single_landmark_s> mappingLandmarks){
	vector<double> weights;
	double std_x = std_landmark[0];
	double std_y = std_landmark[1];

	//cout << "size " << observations.size() << endl;

	for(int k=0; k<observations.size(); k++)
	{
		//cout << "obs " << observations[k].id << endl;
		int id = observations[k].id;
		double x = mappingLandmarks[id].x_f;
		double y = mappingLandmarks[id].y_f;
		double mu_x = observations[k].x;
		double mu_y = observations[k].y;

		double p = exp(-(pow(x-mu_x, 2)/2.0/pow(std_x, 2) + pow(y-mu_y, 2)/2.0/pow(std_y, 2)));
		p = p/2.0/M_PI/std_x/std_y;

		weights.push_back(p);
	}

	return weights;
}
