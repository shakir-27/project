# cd aiotorrent

BRANCH="sync-test-3"

sha_hashes=(
  "c07d084e990660e848176dd175ce7290beeda138"
  "246247fb88d15fbbb6f448d3990121f16622a423"
  "23f634197ba47c684a0dda64b0dc8b33392a5cbd"
  "4d63848c2eb53bb3a2e6df2710bab4f1d5c0ddd9"
  "a4331f18fbaccc6ff1a2488d9c3fcda2c562e580"
  "03dca8b29d3763bea1200464cf94127808bd69c5"
  "a1eb558a8eab1777a25f2aa7de665c66f12f415b"
  "9a7ad76d508bea829575b5d032858ffe6d362e6a"
  "6797c5fa5a89b49c90289235e05ae0fff6532ccb"
  "cd67e21d16e4a080cf2a769a800d03e8920eed25"
  "de000713ad9204347202ab0a254df2cb7250f017"
  "94ae1c715bfd2083ae3df40ed432cd08bc33acb4"
)


for hash in "${sha_hashes[@]}"; do
	message=$(git show 94ae1c715bfd2083ae3df40ed432cd08bc33acb4 | awk "NR == 5" | sed "s/  //g")
	
	while true; do
		read -p "On commit -> ${message} :" input
		if [[ "$input" == "c" ]]; then
			git push origin $hash:refs/heads/sync-test-3
			break
		fi

	done
done
