DOCKER CONTAINER
1. CẤU TẠO DOCKER COMMAND
Cấu trúc lệnh trong Docker

docker <object><command><option>

object là các đối tượng như container, image, volume, network, system.
command là các câu lệnh sử dụng cho các object.
Option là các tham số cho command.

Dưới đây là một ví dụ về cách sử dụng lệnh docker tương tự để chạy một container trong Docker:

docker container run -d --name my-mongo -p 27017:27017 mongo:latest
Giải thích:

docker container run: Chạy một container.
-d: Chạy container ở chế độ nền (detached mode).
--name my-mongo: Đặt tên cho container là "my-mongo".
-p 27017:27017: Mở cổng 27017 trên máy chủ và ánh xạ đến cổng 27017 trong container (thường dùng cho MongoDB).
mongo:latest: Sử dụng image MongoDB mới nhất (latest) từ Docker Hub.
Lệnh này sẽ chạy một container MongoDB với tên "my-mongo", ánh xạ cổng 27017 của container vào cổng 27017 của máy chủ, và chạy ở chế độ nền.


hoặc 1 ví dụ khác:
docker container run -d --name my-nginx -p 80:80 nginx:latest
1. docker container run
docker container run là lệnh dùng để tạo và chạy một container mới từ một image Docker. Lệnh này sẽ tạo một container và bắt đầu thực thi nó.
2. -d (detach mode)
Tùy chọn -d (hoặc --detach) khiến container chạy ở chế độ nền (background). Nếu không có tùy chọn này, Docker sẽ chạy container ở chế độ nền và bạn sẽ phải chạy lệnh docker container stop để dừng container.
Khi chạy ở chế độ nền, bạn sẽ không thấy đầu ra của container trong terminal, nhưng container vẫn sẽ chạy.
3. --name my-nginx
Tùy chọn --name cho phép bạn chỉ định tên cho container. Ở đây, container sẽ có tên là my-nginx.
Nếu không chỉ định tên, Docker sẽ tạo ra một tên ngẫu nhiên cho container.
4. -p 80:80
Tùy chọn -p là để ánh xạ cổng của container với cổng trên máy chủ (host).
Cổng đầu tiên 80 là cổng trên máy chủ (host) mà bạn muốn ánh xạ vào.
Cổng thứ hai 80 là cổng mà container đang sử dụng.
Điều này có nghĩa là khi bạn truy cập vào cổng 80 trên máy chủ (ví dụ, http://localhost:80), bạn sẽ được chuyển đến cổng 80 trong container, nơi Nginx đang lắng nghe và phục vụ nội dung.
5. nginx:latest
Đây là tên của image Docker mà bạn muốn sử dụng để tạo container.
nginx là tên image.
latest là tag, chỉ phiên bản mới nhất của image Nginx.
Nếu không có tag, Docker sẽ mặc định sử dụng phiên bản "latest".
Tóm lại:
Lệnh này tạo và chạy một container Nginx từ image nginx:latest, đặt tên cho container là my-nginx, và ánh xạ cổng 80 của container với cổng 80 trên máy chủ. Container sẽ chạy ở chế độ nền (background).


Một số cổng phổ biến được sử dụng trong Docker cho các dịch vụ khác nhau:

MySQL:

Cổng mặc định: 3306
Lệnh:

docker container run -d --name my-mysql -p 3306:3306 mysql:latest
PostgreSQL:

Cổng mặc định: 5432
Lệnh:

docker container run -d --name my-postgres -p 5432:5432 postgres:latest
Redis:

Cổng mặc định: 6379
Lệnh:

docker container run -d --name my-redis -p 6379:6379 redis:latest
Nginx:

Cổng mặc định: 80 (HTTP) hoặc 443 (HTTPS)
Lệnh:

docker container run -d --name my-nginx -p 80:80 nginx:latest
MongoDB:

Cổng mặc định: 27017
Lệnh:

docker container run -d --name my-mongo -p 27017:27017 mongo:latest
Apache HTTP Server:

Cổng mặc định: 80
Lệnh:

docker container run -d --name my-apache -p 80:80 httpd:latest
Elasticsearch:

Cổng mặc định: 9200 (HTTP), 9300 (Transport)
Lệnh:

docker container run -d --name my-elasticsearch -p 9200:9200 -p 9300:9300 docker.elastic.co/elasticsearch/elasticsearch:latest
Jenkins:

Cổng mặc định: 8080
Lệnh:

docker container run -d --name my-jenkins -p 8080:8080 jenkins/jenkins:lts
RabbitMQ:

Cổng mặc định: 5672 (AMQP), 15672 (HTTP Management)
Lệnh:

docker container run -d --name my-rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
GitLab:

Cổng mặc định: 80 (HTTP)
Lệnh:

docker container run -d --name my-gitlab -p 80:80 gitlab/gitlab-ce:latest



Ngoài ra còn có thể sử dụng phím tắt
docker ps, docker container ls
docker pull: pull (download) một docker ioimage
docker version: hiển thị phiên bản của Docker client, docker host.

2. TẠO CONTAINER ĐẦU TIÊN



3. KHÁM PHÁ CONTAINER



4. CONTAINER VSS VIRTUAL MACHINE







IMAGE VS CONTAINER
1. Docker image là file template tạo ra container
2. Container là môi trường ảo hóa độc lập, hoàn chỉnh chứa chương trình và các gói bổ sung
3. Container bản chất là một process trên hệ thống