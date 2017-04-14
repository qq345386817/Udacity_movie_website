#-*- coding: UTF-8 -*-

import fresh_tomatoes
import media

kong_skull_island = media.Movie("Kong: Skull Island", "1:32", "When a scientific expedition to an uncharted island awakens titanic forces of nature, a mission of discovery becomes an explosive war between monster and man. Tom Hiddleston, Samuel L. Jackson, Brie Larson, John Goodman and John C. Reilly star in a thrilling and original adventure that reveals the untold story of how Kong became King.", "https://i.ytimg.com/vi/GviRHm6hI0I/movieposter.jpg", "https://www.youtube.com/watch?v=GviRHm6hI0I")

zootopia = media.Movie("Zootopia", "1:32", "Disney presents a heartwarming comedy-adventure set in the modern mammal metropolis of Zootopia. With habitat neighborhoods like ritzy Sahara Square and frigid Tundratown, it’s a melting pot where animals from every environment live together—a place where no matter what you are, from the biggest elephant to the smallest shrew, you can be anything. But when optimistic Officer Judy Hopps arrives, she discovers that being the first bunny on a police force of big, tough animals isn’t so easy. Determined to prove herself, she jumps at the opportunity to crack a case, even if it means partnering with fast-talking scam-artist fox Nick Wilde to solve the mystery.", "https://i.ytimg.com/vi/d4WEUn0yS74/movieposter.jpg", "https://www.youtube.com/watch?v=d4WEUn0yS74")

logan = media.Movie("Logan", "1:32", "In the near future, a weary Logan cares for an ailing Professor X in a hide out on the Mexican border. But Logan's attempts to hide from the world and his legacy are up-ended when a young mutant arrives, being pursued by dark forces.", "https://i.ytimg.com/vi/GmCV6BCqG4E/movieposter.jpg", "https://www.youtube.com/watch?v=GmCV6BCqG4E")

jackie = media.Movie("Jackie", "1:32", "Natalie Portman stars in this powerfully stirring drama as First Lady Jacqueline Kennedy, whose faith and strength see her through the death of President John F. Kennedy.", "https://i.ytimg.com/vi/g7VZ3sYL_bs/movieposter.jpg", "https://www.youtube.com/watch?v=g7VZ3sYL_bs")

the_lego_betman_movie = media.Movie("The LEGO® Batman Movie", "1:32", "In the irreverent spirit of fun that made “The LEGO® Movie” a worldwide phenomenon, the self-described leading man of that ensemble – LEGO Batman (Will Arnett) – stars in his own big-screen adventure. But there are big changes brewing in Gotham, and if he wants to save the city from The Joker’s (Zach Galifianakis) hostile takeover, Batman may have to drop the lone vigilante thing, try to work with others and maybe, just maybe, learn to lighten up.", "https://i.ytimg.com/vi/_pc2-y8WJn8/movieposter.jpg", "https://www.youtube.com/watch?v=_pc2-y8WJn8")

hidden_figures = media.Movie("Hidden Figures", "1:32", "The incredible untold true story of Katherine Johnson (Taraji P. Henson), Dorothy Vaughan (Octavia Spencer) & Mary Jackson (Janelle Monae)—brilliant African-American women working at NASA, who served as the brains behind one of the greatest operations in history: the launch of astronaut John Glenn into orbit. This stunning achievement galvanized the world and inspired generations to dream big.", "https://i.ytimg.com/vi/U386EMeWo3I/movieposter.jpg", "https://www.youtube.com/watch?v=U386EMeWo3I")

movies = [kong_skull_island, zootopia, logan, jackie, the_lego_betman_movie, hidden_figures]

fresh_tomatoes.open_movies_page(movies)
