default:

hello:
	dagger -v -i -c "hello ."

none:
	dagger -v -i -c "none"

wget:
	dagger -v -i -c "wget | terminal --cmd bash"

shell:
	dagger -v -i -c "shell . | terminal --cmd bash"

huge:
	dagger -v -i -c "mount-huge ./ | terminal --cmd bash"

install_huge:
	dagger -v -i -c "install-huge | terminal --cmd bash"

use:
	dagger -v -i -c "use-huge-image | stdout"

clear:
	docker system prune -a --volumes

purge:
	docker builder prune

reset:
	docker container stop dagger-engine-v0.18.16
	docker container rm dagger-engine-v0.18.16
	docker system prune -a --volumes

df:
	docker system df | tee -a df.txt

df_loop:
	while true; do \
		docker system df; \
		sleep 2; \
		done

vol:
	docker volume ls

inspect:
	docker volume inspect <ID>


.PNOHY: default hello none wget shell huge install_huge use
.PNOHY: clear purge reset df df_loop vol inspect
